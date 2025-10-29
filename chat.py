from chat import summarize_chat, save_meta_prompt, clear_history_file

CHAT_HISTORY_FILE = "chat_history.json"

def main():
    # Clear old chat history at start
    clear_history_file(CHAT_HISTORY_FILE)

    chat_history = []

    print("🧙 Gemini Chat — type 'summary' to save meta prompt, 'quit' to exit.")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            break
        elif user_input.lower() == "summary":
            summary = summarize_chat(chat_history)
            save_meta_prompt(summary)
            print("\n✅ Meta prompt saved!")
        else:
            # Chat logic (append to in-memory chat_history)
            reply = "..."  # replace with chat_with_gemini() if needed
            chat_history.append({"role": "user", "content": user_input})
            chat_history.append({"role": "assistant", "content": reply})
            print(f"\nGemini: {reply}")

if __name__ == "__main__":
    main()
