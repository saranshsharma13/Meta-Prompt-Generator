from chat import chat_with_gemini, summarize_chat, save_meta_prompt, clear_history_file
from config import SUMMARIZE_AFTER, CHAT_LOG_FILE, PERSONAS
import argparse

def main():
    parser = argparse.ArgumentParser(description="Gemini Chat with Personas")
    parser.add_argument("--persona", choices=PERSONAS.keys(), default="friendly",
                        help="Choose assistant persona")
    args = parser.parse_args()

    persona = args.persona
    print(f"🧙 Gemini Chat Summarizer — Persona: {persona} ({PERSONAS[persona]['description']})")
    print("Type 'summary' to compress, 'quit' to exit.\n")

    # Clear old chat log
    clear_history_file(CHAT_LOG_FILE)

    chat_history = []  # in-memory only

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("👋 Goodbye!")
            break
        elif user_input.lower() == "summary":
            summary = summarize_chat(chat_history, persona)
            save_meta_prompt(summary, persona)
            print("\n🧩 META PROMPT SUMMARY SAVED:\n")
            print(summary)
            continue

        reply = chat_with_gemini(user_input, chat_history, persona)
        print(f"\nGemini: {reply}\n")

        if len(chat_history) >= SUMMARIZE_AFTER * 2:
            print("\n⚙️ Conversation getting long — auto-generating summary...\n")
            summary = summarize_chat(chat_history, persona)
            save_meta_prompt(summary, persona)
            print(summary)
            # Reset chat to only meta summary
            chat_history = [{"role": "system", "content": summary}]
            print("\n✅ Context compressed — continuing chat.\n")


if __name__ == "__main__":
    main()
