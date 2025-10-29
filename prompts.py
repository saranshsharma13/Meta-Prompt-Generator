# Prompt templates for Gemini

META_SUMMARY_PROMPT = """
You are a meta-prompt generator.
Summarize the following full conversation into a concise meta prompt that preserves:
- Goals
- Key facts
- Tone and context
- Style and constraints
Make the result reusable as a starting prompt for future sessions.

Conversation:
{conversation}

Output format:
### Meta Prompt
[Your summary here]
"""
