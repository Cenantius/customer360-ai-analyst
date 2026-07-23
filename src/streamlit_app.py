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

question = st.text_input(
    "Question",
    placeholder="Which customers have the highest lifetime value?"
)

ask_button = st.button("Ask database")

if ask_button:
    if not question.strip():
        st.warning("Enter a question first.")
    else:
        try:
            with st.spinner("Analyzing the database..."):
                result = ask_database(question)

            st.subheader("Answer")
            st.write(result.answer)

            st.subheader("Query result")
            st.dataframe(
                result.data,
                use_container_width=True,
            )

            with st.expander("Generated SQL"):
                st.code(result.sql, language="sql")

        except Customer360Error as error:
            st.error(str(error))