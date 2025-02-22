MODEL_CHOICES = {
    "1": {"name": "google/flan-t5-small", "type": "seq2seq", "params": "80M"},
    "2": {"name": "google/flan-t5-base", "type": "seq2seq", "params": "250M"},
    "3": {"name": "google/flan-t5-large", "type": "seq2seq", "params": "780M"},
    "4": {"name": "sshleifer/distilbart-cnn-12-6", "type": "seq2seq", "params": "306M"},
    "5": {"name": "facebook/bart-large-cnn", "type": "seq2seq", "params": "406M"},
    "6": {"name": "lidiya/bart-large-xsum-samsum", "type": "seq2seq", "params": "406M"},
    "9": {"name": "google/flan-t5-xl", "type": "seq2seq", "params": "3B"},
    "10": {"name": "google/flan-t5-xxl", "type": "seq2seq", "params": "11B"},
    "11": {"name": "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", "type": "causal", "params": "1B"},
    "12": {"name": "Qwen/Qwen2.5-14B", "type": "causal", "params": "7B"},
}

def get_model_choices():
    return MODEL_CHOICES