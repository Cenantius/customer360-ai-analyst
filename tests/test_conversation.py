from conversation import build_conversation_context


def test_builds_context_from_completed_turn() -> None:
    messages = [
        {
            "role": "user",
            "content": "Which city generated the most revenue?",
        },
        {
            "role": "assistant",
            "content": "Jyväskylä generated the most revenue.",
            "sql": "SELECT city FROM customer_lifetime_value;",
        },
    ]

    context = build_conversation_context(messages)

    assert "Which city generated the most revenue?" in context
    assert "Jyväskylä generated the most revenue." in context
    assert "SELECT city" in context

def test_ignores_incomplete_user_turn() -> None:
    messages = [
        {
            "role": "user",
            "content": "Which city generated the most revenue?",
        },
        {
            "role": "assistant",
            "content": "Jyväskylä generated the most revenue.",
            "sql": "SELECT city FROM customer_lifetime_value;",
        },
        {
            "role": "user",
            "content": "What about Helsinki?",
        },
    ]

    context = build_conversation_context(messages)

    assert "Which city generated the most revenue?" in context
    assert "What about Helsinki?" not in context

def test_limits_context_to_max_turns() -> None:
    messages = [
        {
            "role": "user",
            "content": "Question 1",
        },
        {
            "role": "assistant",
            "content": "Answer 1",
            "sql": "SELECT 1;",
        },
        {
            "role": "user",
            "content": "Question 2",
        },
        {
            "role": "assistant",
            "content": "Answer 2",
            "sql": "SELECT 2;",
        },
        {
            "role": "user",
            "content": "Question 3",
        },
        {
            "role": "assistant",
            "content": "Answer 3",
            "sql": "SELECT 3;",
        },
    ]

    context = build_conversation_context(
        messages,
        max_turns=2,
    )

    assert "Question 1" not in context
    assert "Question 2" in context
    assert "Question 3" in context
