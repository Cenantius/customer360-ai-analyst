import pytest

from sql_validator import validate_sql


def test_accepts_valid_select_query() -> None:
    query = "SELECT * FROM customers;"

    result = validate_sql(query)

    assert result == query


def test_rejects_empty_query() -> None:
    with pytest.raises(
        ValueError,
        match="The generated SQL query is empty.",
    ):
        validate_sql("")


def test_rejects_delete_query() -> None:
    with pytest.raises(
        ValueError,
        match="Only SELECT queries are allowed.",
    ):
        validate_sql("DELETE FROM customers;")


def test_rejects_update_query() -> None:
    with pytest.raises(
        ValueError,
        match="Only SELECT queries are allowed.",
    ):
        validate_sql(
            "UPDATE customers SET city = 'Helsinki';"
        )


def test_rejects_multiple_statements() -> None:
    query = (
        "SELECT * FROM customers; "
        "DELETE FROM customers;"
    )

    with pytest.raises(ValueError):
        validate_sql(query)