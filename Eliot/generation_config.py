GENERATION_CONFIG = {
    "seq2seq":{
        "do_sample": True,
        "temperature": 0.9,
        "top_p": 0.90,
        "max_new_tokens": 512,
        "repetition_penalty": 1.0,
    },
    "summarize": {
        "temperature": 0.5,
        "top_p": 0.92,
        "top_k": 40,
        "max_new_tokens": 1024,
        "repetition_penalty": 1.25,
        "do_sample": True,
        "num_beams": 1,
    },
    "analyze": {
        "temperature": 0.6,
        "top_p": 0.85,
        "max_new_tokens": 1024,
        "repetition_penalty": 1.8,
        "do_sample": True,
        "num_beams": 1,
    },
    "opinion": {
        "temperature": 0.6,
        "top_p": 0.95,
        "max_new_tokens": 1024,
        "repetition_penalty": 1.8,
        "do_sample": True,
        "num_beams": 1,
    }
}

def get_generation_config():
    return GENERATION_CONFIG