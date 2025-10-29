# Meta-Prompt-Generator

A lightweight Python tool that lets you **chat with Google Gemini** in real time using a low-cost model, and automatically **compress your conversation into a reusable meta-prompt** using a high-end model. Ideal for context-aware workflows, workshops, or AI-assisted brainstorming.

---

## ✨ Features

* 💬 **Real-Time Chat** — Talk to Gemini using a low-cost, fast model (`gemini-2.0-flash`).
* 🧩 **Meta-Prompt Summarization** — Compress long conversations into a concise meta prompt with a high-end model (`gemini-2.5-pro`).
* 🔄 **Automatic Context Compression** — Keeps chat context manageable and reusable.
* 💾 **Persistent Sessions** — Stores your chat history locally in JSON.
* ⚙️ **Modular Structure** — Config, prompts, and chat logic separated for easy maintenance.

---

## 🗂 Project Structure

```
.
├── config.py          # Configuration and environment variables
├── prompts.py         # Prompt templates for summarization
├── chat.py            # Core chat and summarization logic
├── main.py            # Entry point: chat loop
├── chat_history.json  # Stored chat sessions (auto-generated)
└── README.md
```

---

## ⚙️ Setup

1. Clone the repo:

```bash
git clone <your-repo-url>
cd <repo-directory>
```

2. Install dependencies:

```bash
pip install google-genai
```

3. Optionally, set environment variables:

```
GEMINI_API_KEY=your_api_key
CHAT_MODEL=gemini-2.0-flash
SUMMARY_MODEL=gemini-2.5-pro
SUMMARIZE_AFTER=10
CHAT_LOG_FILE=chat_history.json
```

---

## 🧑‍💻 Usage

Run the chat:

```bash
python main.py
```

### Commands inside chat:

* Type your message to chat with Gemini.
* `summary` → Forces immediate meta-prompt summarization.
* `quit` → Exit the program.

When your conversation exceeds the configured message threshold, it will **auto-generate a summary** and continue with the compressed context.

---

## 🔧 Customization

* Adjust chat and summarizer models in `config.py` or via environment variables.
* Modify the meta-prompt in `prompts.py` to tweak summarization style.
* Change `SUMMARIZE_AFTER` to control auto-summary frequency.

---
