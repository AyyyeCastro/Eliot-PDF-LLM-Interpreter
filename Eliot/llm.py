import fitz
import torch
import re
import os
from transformers import (
    pipeline,
    AutoTokenizer,
    AutoModelForCausalLM,
    AutoModelForSeq2SeqLM,
)
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from task_templates import get_task_templates
from generation_config import get_generation_config
from model_choices import get_model_choices
from instructions import get_instructions

app = Flask(__name__)

# --- Configuration ---
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- Enhanced Configuration ---
TASK_TEMPLATES = get_task_templates()
GENERATION_CONFIG = get_generation_config()


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_from_pdf(file_path):
    try:
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += f"PAGE {page.number+1}: {page.get_text()}\n"
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None


def chunk_text(text, tokenizer, max_chunk_size=2048):
    tokens = tokenizer(text, return_tensors="pt", truncation=False)
    total_tokens = tokens.input_ids.shape[1]
    return [
        tokenizer.decode(
            tokens.input_ids[0][i : i + max_chunk_size], skip_special_tokens=True
        )
        for i in range(0, total_tokens, max_chunk_size)
    ]


def build_prompt(
    model_type, task_type, chunk, context_history, custom_prompt=None, tokenizer=None
):
    template = TASK_TEMPLATES[task_type]

    if model_type == "seq2seq":
        base_prompt = TASK_TEMPLATES["seq2seq"]["system_prompt"]
        context = "\n".join(context_history[-3:])
        return f"{base_prompt}{context}\n{chunk}"

    # Causal model prompt (Qwen specific)
    system_msg = template["system_prompt"]
    if custom_prompt:
        system_msg = f"{system_msg}. {custom_prompt}"

    instructions = get_instructions()

    prompt = f"<|im_start|>system\n{system_msg}<|im_end|>\n"
    prompt += f"<|im_start|>user\n[CONTEXT]\n{chr(10).join(context_history[-3:])}\n\n[TEXT]\n{chunk}\n\n[INSTRUCTIONS]\n{instructions}<|im_end|>\n"  # User message
    prompt += f"<|im_start|>assistant\n"

    return prompt


def validate_output(text, original_text):
    violations = []
    quotes = re.findall(r"\(p\.\d+\)", text)
    for q in quotes:
        page = int(q.split(".")[1][:-1])
        if f"PAGE {page}:" not in original_text:
            violations.append(f"Invalid page reference: {q}")
    return violations


# --- Model Choices ---
MODEL_CHOICES = get_model_choices()


@app.route("/", methods=["GET", "POST"])
def index():
    tasks = list(TASK_TEMPLATES.keys())
    # Corrected sorting logic
    sorted_models = dict(
        sorted(
            MODEL_CHOICES.items(),
            key=lambda x: int(x[1]["params"].replace("M", "").replace("B", "")),
        )
    )
    return render_template("index.html", tasks=tasks, model_choices=sorted_models)


@app.route("/docs")
def docs():
    """Renders the documentation page."""
    return render_template("docs.html")


@app.route("/credits")
def credits():
    """Renders the creditation page."""
    sorted_models = dict(
        sorted(
            MODEL_CHOICES.items(),
            key=lambda x: int(x[1]["params"].replace("M", "").replace("B", "")),
        )
    )
    return render_template("credit.html", model_choices=sorted_models)


@app.route("/process", methods=["POST"])
def process_document():
    if "pdfFile" not in request.files:
        return jsonify({"error": "No PDF file"}), 400
    file = request.files["pdfFile"]
    if not file or not allowed_file(file.filename):
        return jsonify({"error": "Invalid file"}), 400

    model_choice = request.form.get("modelChoice")
    task_type = request.form.get("taskType", "summarize")
    user_prompt = request.form.get("prompt", "")

    if model_choice not in MODEL_CHOICES:
        return jsonify({"error": "Invalid model"}), 400

    model_info = MODEL_CHOICES[model_choice]
    model_type = model_info["type"]

    # Handle prompt selection
    default_prompt = TASK_TEMPLATES[task_type]["system_prompt"]
    selected_prompt = user_prompt if model_type == "causal" else default_prompt

    # File processing
    filename = secure_filename(file.filename)
    pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(pdf_path)
    text_content = extract_from_pdf(pdf_path)
    os.remove(pdf_path)

    if not text_content:
        return jsonify({"error": "Text extraction failed"}), 500

    # Model loading
    try:
        tokenizer = AutoTokenizer.from_pretrained(
            model_info["name"], trust_remote_code=True
        )
        if model_type == "seq2seq":
            model = AutoModelForSeq2SeqLM.from_pretrained(
                model_info["name"], device_map="auto", torch_dtype=torch.float16
            )
            summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
        else:
            model = AutoModelForCausalLM.from_pretrained(
                model_info["name"],
                device_map="auto",
                torch_dtype=torch.float16,
                trust_remote_code=True,
            )
    except Exception as e:
        return jsonify({"error": f"Model load failed: {str(e)}"}), 500

    chunks = chunk_text(text_content, tokenizer)
    context_history = []
    output_parts = []

    for chunk in chunks:
        if model_type == "seq2seq":
            prompt = build_prompt(
                model_type, task_type, chunk, context_history, tokenizer=tokenizer
            )
            inputs = tokenizer([prompt], return_tensors="pt", padding=True).to(
                model.device
            )
            outputs = model.generate(**inputs, **GENERATION_CONFIG[task_type])
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(f"DEBUG - Raw response: {response}")
        else:
            prompt = build_prompt(
                model_type,
                task_type,
                chunk,
                context_history,
                selected_prompt,
                tokenizer=tokenizer,
            )
            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
            outputs = model.generate(
                **inputs,
                **GENERATION_CONFIG[task_type],
                eos_token_id=tokenizer.eos_token_id,
            )  # ADD eos_token_id here
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(f"DEBUG - Raw response: {response}")

            assistant_start_token = "<|im_start|>assistant"
            if assistant_start_token in response:
                response = response.split(assistant_start_token)[1].strip()
            else:
                print("WARNING: Assistant start token not found!")
            response = response.strip()

        # Context and validation
        verified_quotes = re.findall(r"\(p\.\d+\)", response)
        context_history.extend(verified_quotes)
        output_parts.append(response)

    # Post-processing
    full_output = "\n\n".join(output_parts)
    violations = validate_output(full_output, text_content)

    if violations:
        full_output += "\n\nVALIDATION ISSUES:\n- " + "\n- ".join(violations)

    if model_type == "causal" and task_type == "opinion":
        full_output += "\n\nNOTE: Analysis based on document content only."

    return jsonify({"result": full_output.strip()})


if __name__ == "__main__":
    app.run(debug=True)
