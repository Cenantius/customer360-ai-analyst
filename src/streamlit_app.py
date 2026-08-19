import streamlit as st

from conversation import build_conversation_context
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
        
        if message.get("execution_time") is not None:
            st.caption(
                f"Completed in {message['execution_time']:.2f} seconds"
            )

        if message.get("data") is not None:
            st.dataframe(
                message["data"],
                width=True,
            )

        if message.get("sql"):
            with st.expander("Generated SQL"):
                st.code(message["sql"], language="sql")


question = st.chat_input(
    "Ask a question about Customer360 data"
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

                conversation_context = build_conversation_context(
                    st.session_state.messages,
                    max_turns=3,
                )

                result = ask_database(
                    question,
                    conversation_context=conversation_context,
                )

            st.write(result.answer)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": result.answer,
                    "data": result.data,
                    "sql": result.sql,
                    "execution_time": result.execution_time,
                }
            )

            st.dataframe(
                result.data,
                width=True,
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