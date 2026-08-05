import streamlit as st

from exceptions import Customer360Error
from logging_config import configure_logging
from pipeline import ask_database


configure_logging()

st.set_page_config(
    page_title="Customer360 AI Analyst",
    page_icon="📊",
    layout="wide",
)

st.title("Customer360 AI Analyst")
st.write(
    "Ask a natural-language question about the Customer360 database."
)

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

        if message.get("data") is not None:
            st.dataframe(
                message["data"],
                use_container_width=True,
            )

        if message.get("sql"):
            with st.expander("Generated SQL"):
                st.code(message["sql"], language="sql")


question = st.text_input(
    "Question",
    placeholder="Which customers have the highest lifetime value?"
)

if question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Analyzing the database..."):
                result = ask_database(question)

            st.write(result.answer)

            st.dataframe(
                result.data,
                use_container_width=True,
            )

            with st.expander("Generated SQL"):
                st.code(result.sql, language="sql")

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": result.answer,
                    "data": result.data,
                    "sql": result.sql,
                }
            )

        except Customer360Error as error:
            error_message = str(error)

            st.error(error_message)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_message
                }
            )