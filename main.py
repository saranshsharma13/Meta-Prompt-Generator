from chat import chat_with_gemini, summarize_chat, clear_history_file, save_meta_prompt
from config import SUMMARIZE_AFTER, CHAT_LOG_FILE

def main():
    print("🧙 Gemini Chat Summarizer — type 'summary' to compress, 'quit' to exit.\n")
    
    # Clear full chat history JSON at start
    clear_history_file(CHAT_LOG_FILE)

    chat_history = []  # keep chat in-memory only

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("👋 Goodbye!")
            break
        elif user_input.lower() == "summary":
            summary = summarize_chat(chat_history)
            save_meta_prompt(summary)  # save only meta summary
            print("\n🧩 META PROMPT SUMMARY SAVED:\n")
            print(summary)
            continue

        # Generate reply and append to in-memory history
        reply = chat_with_gemini(user_input, chat_history)
        print(f"\nGemini: {reply}\n")

        # Auto-summarize if conversation is long
        if len(chat_history) >= SUMMARIZE_AFTER * 2:
            print("\n⚙️ Conversation getting long — auto-generating summary...\n")
            summary = summarize_chat(chat_history)
            save_meta_prompt(summary)  # store meta summary
            print(summary)
            # Reset chat to just meta summary context
            chat_history = [{"role": "system", "content": summary}]
            print("\n✅ Context compressed — continuing chat.\n")
