from google import genai
from google.genai import types
import json
import os
from config import CHAT_MODEL, SUMMARY_MODEL, META_PROMPT_FILE, PERSONAS

# Initialize client
client = genai.Client()

# --------------------------
# CORE FUNCTIONS
# --------------------------


def generate_with_model(model_name, prompt):
    """Generate response from Gemini model."""
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)),
    )
    return getattr(response, "text", str(response))


def chat_with_gemini(user_input, chat_history, persona_name="friendly"):
    persona_prompt = PERSONAS[persona_name]["meta_prompt"]
    messages = "\n".join(
        [f"{m['role'].capitalize()}: {m['content']}" for m in chat_history])
    prompt = f"{persona_prompt}\n{messages}\nUser: {user_input}\nAssistant:"
    reply = generate_with_model(CHAT_MODEL, prompt)
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": reply})
    return reply


def summarize_chat(chat_history, persona="friendly"):
    """Summarize chat into a meta prompt using selected persona."""
    full_chat = "\n".join(
        [f"{m['role'].capitalize()}: {m['content']}" for m in chat_history])
    persona_prompt = PERSONAS.get(persona, PERSONAS["friendly"])["meta_prompt"]
    prompt = persona_prompt.format(conversation=full_chat)
    summary = generate_with_model(SUMMARY_MODEL, prompt)
    return summary


def save_meta_prompt(summary, persona="friendly"):
    """Append meta prompt summary to JSON file."""
    meta_prompts = []
    if os.path.exists(META_PROMPT_FILE):
        with open(META_PROMPT_FILE, "r") as f:
            meta_prompts = json.load(f)
    meta_prompts.append({"persona": persona, "summary": summary})
    with open(META_PROMPT_FILE, "w") as f:
        json.dump(meta_prompts, f, indent=2)


def clear_history_file(file_path):
    """Clear a JSON file at start of session."""
    with open(file_path, "w") as f:
        json.dump([], f)
