from chat import chat_with_gemini, summarize_chat, load_chat, save_chat
from config import SUMMARIZE_AFTER

def main():
    print("🧙 Gemini Chat Summarizer — type 'summary' to compress, 'quit' to exit.\n")
    chat_history = load_chat()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("👋 Goodbye!")
            break
        elif user_input.lower() == "summary":
            summary = summarize_chat(chat_history)
            print("\n🧩 META PROMPT SUMMARY:\n")
            print(summary)
            continue

        reply = chat_with_gemini(user_input, chat_history)
        print(f"\nGemini: {reply}\n")

        # Auto-summarize if conversation is long
        if len(chat_history) >= SUMMARIZE_AFTER * 2:
            print("\n⚙️ Conversation getting long — auto-generating summary...\n")
            summary = summarize_chat(chat_history)
            print(summary)
            chat_history = [{"role": "system", "content": summary}]
            print("\n✅ Context compressed — continuing chat.\n")

        save_chat(chat_history)


if __name__ == "__main__":
    main()
