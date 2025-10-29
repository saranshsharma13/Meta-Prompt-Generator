from google import genai
from google.genai import types
import json
import os
from config import SUMMARY_MODEL, META_PROMPT_FILE
from prompts import META_SUMMARY_PROMPT

# Initialize client
client = genai.Client()

# --------------------------
# CORE FUNCTIONS
# --------------------------

def generate_with_model(model_name, prompt, thinking_budget=500):
    """Generate response from a Gemini model."""
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=thinking_budget)
        ),
    )
    return getattr(response, "text", str(response))


def summarize_chat(chat_history):
    """Generate meta prompt summary from full chat (in-memory)."""
    full_chat = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in chat_history])
    prompt = META_SUMMARY_PROMPT.format(conversation=full_chat)
    summary = generate_with_model(SUMMARY_MODEL, prompt)
    return summary


def save_meta_prompt(summary):
    """Append meta summary to META_PROMPT_FILE."""
    data = []
    if os.path.exists(META_PROMPT_FILE):
        with open(META_PROMPT_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    data.append({"meta_prompt": summary})
    with open(META_PROMPT_FILE, "w") as f:
        json.dump(data, f, indent=2)


def clear_history_file(file_path):
    """Clear a JSON file at the start of a run."""
    with open(file_path, "w") as f:
        json.dump([], f)
