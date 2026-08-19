def build_conversation_context(
    messages: list[dict],
    max_turns: int = 3,
) -> str:
    """
    Builds a compact context string from recent completed chat turns.
    """

    completed_turns = []
    pending_question = None

    for message in messages:
        role = message.get("role")
        content = message.get("content", "")

        if role == "user":
            pending_question = content

        elif role == "assistant" and pending_question is not None:
            completed_turns.append(
                {
                    "question": pending_question,
                    "answer": content,
                    "sql": message.get("sql", ""),
                }
            )

            pending_question = None

    recent_turns = completed_turns[-max_turns:]
    context_sections = []

    for turn_number, turn in enumerate(recent_turns, start=1):
        section = (
            f"Previous turn {turn_number}:\n"
            f"User question: {turn['question']}\n"
            f"Generated SQL: {turn['sql']}\n"
            f"Answer: {turn['answer']}"
        )

        context_sections.append(section)

    return "\n\n".join(context_sections)