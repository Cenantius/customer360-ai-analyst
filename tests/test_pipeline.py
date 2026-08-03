import pandas as pd

from pipeline import ask_database


def test_pipeline_uses_injected_dependencies() -> None:
    expected_question = "Who is the highest-value customer?"
    generated_sql = "SELECT * FROM customer_lifetime_value LIMIT 1;"
    safe_sql = "SELECT * FROM customer_lifetime_value LIMIT 1;"

    expected_data = pd.DataFrame(
        [
            {
                "first_name": "Derek",
                "last_name": "Johnson",
                "total_completed_revenue": 1831.76,
            }
        ]
    )

    expected_answer = (
        "Derek Johnson is the highest-value customer "
        "with 1831.76 in completed revenue."
    )

    def fake_generate_sql(question: str) -> str:
        assert question == expected_question
        return generated_sql

    def fake_validate_sql(received_sql: str) -> str:
        assert received_sql == generated_sql
        return safe_sql

    def fake_run_query(received_sql: str) -> pd.DataFrame:
        assert received_sql == safe_sql
        return expected_data

    def fake_analyze_results(
        question: str,
        results: str,
    ) -> str:
        assert question == expected_question
        assert "Derek" in results
        assert "1831.76" in results

        return expected_answer

    result = ask_database(
        expected_question,
        sql_generator=fake_generate_sql,
        sql_validator=fake_validate_sql,
        query_runner=fake_run_query,
        result_analyzer=fake_analyze_results,
    )

    assert result.question == expected_question
    assert result.sql == safe_sql
    assert result.data.equals(expected_data)
    assert result.answer == expected_answer