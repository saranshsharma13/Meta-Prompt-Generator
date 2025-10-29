from google import genai
from google.genai import types
import json
import os
from config import CHAT_MODEL, SUMMARY_MODEL, CHAT_LOG_FILE
from prompts import META_SUMMARY_PROMPT

# Initialize client
client = genai.Client()

# --------------------------
# CORE FUNCTIONS
# --------------------------

def generate_with_model(model_name, prompt):
    """Generate response from a specific Gemini model."""
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        ),
    )
    return getattr(response, "text", str(response))

def chat_with_gemini(user_input, chat_history):
    """Chat using low-end Gemini model."""
    messages = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in chat_history])
    prompt = f"{messages}\nUser: {user_input}\nAssistant:"
    reply = generate_with_model(CHAT_MODEL, prompt)
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": reply})
    return reply

def summarize_chat(chat_history):
    """Summarize conversation into a meta prompt using high-end model."""
    full_chat = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in chat_history])
    prompt = META_SUMMARY_PROMPT.format(conversation=full_chat)
    summary = generate_with_model(SUMMARY_MODEL, prompt)
    return summary

def save_chat(chat_history):
    """Save chat to local JSON."""
    with open(CHAT_LOG_FILE, "w") as f:
        json.dump(chat_history, f, indent=2)

def load_chat():
    """Load previous chat if exists."""
    if os.path.exists(CHAT_LOG_FILE):
        with open(CHAT_LOG_FILE, "r") as f:
            return json.load(f)
    return []
