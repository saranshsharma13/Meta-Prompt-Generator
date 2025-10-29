import os

# --------------------------
# CONFIGURATION
# --------------------------

CHAT_MODEL = os.getenv("CHAT_MODEL", "gemini-2.0-flash")        # low-cost, fast chat
SUMMARY_MODEL = os.getenv("SUMMARY_MODEL", "gemini-2.5-flash")    # high-end summarizer
SUMMARIZE_AFTER = int(os.getenv("SUMMARIZE_AFTER", 10))        # summarize after N messages
CHAT_LOG_FILE = os.getenv("CHAT_LOG_FILE", "chat_history.json")
