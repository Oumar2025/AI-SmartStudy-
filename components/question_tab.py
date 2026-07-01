import streamlit as st


def show_question_tab(
    vector_store,
    search_document,
    answer_question
):

    st.subheader("💬 Ask Questions")

    st.write(
        "Ask anything about the uploaded PDF."
    )

    question = st.text_input(
        "Enter your question",
        key="question_input"
    )

    if st.button(
        "Get Answer",
        key="answer_button"
    ):

        if question.strip() == "":

            st.warning("Please enter a question.")

            return

        with st.spinner("Searching document..."):

            context = search_document(
                vector_store,
                question
            )

            answer = answer_question(
                question,
                context
            )

        st.subheader("Answer")

        st.write(answer)