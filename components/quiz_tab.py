import streamlit as st


def show_quiz_tab(text, generate_quiz):

    st.subheader("📝 Smart Quiz")

    # ---------- Session State ----------
    if "quiz" not in st.session_state:
        st.session_state.quiz = None

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "answered" not in st.session_state:
        st.session_state.answered = False

    # ---------- Generate Quiz ----------
    if st.button("Generate Quiz", key="quiz_button"):

        with st.spinner("Creating quiz..."):

            st.session_state.quiz = generate_quiz(text)

            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.answered = False

    # ---------- No Quiz Yet ----------
    if not st.session_state.quiz:
        return

    quiz = st.session_state.quiz

    # ---------- Quiz Finished ----------
    if st.session_state.current_question >= len(quiz):

        st.balloons()

        st.success(
            f"🎉 Quiz Finished!\n\nScore: {st.session_state.score}/{len(quiz)}"
        )

        if st.button("Restart Quiz"):

            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.answered = False

            st.rerun()

        return

    # ---------- Current Question ----------
    q = quiz[st.session_state.current_question]

    st.success(
        f"Question {st.session_state.current_question + 1} of {len(quiz)}"
    )

    answer = st.radio(
        q["question"],
        ["A", "B", "C", "D"],
        format_func=lambda x: f"{x}) {q['options'][x]}",
        key=f"radio_{st.session_state.current_question}",
    )

    if not st.session_state.answered:

        if st.button("Submit Answer"):

            st.session_state.answered = True

            if answer == q["answer"]:

                st.session_state.score += 1

                st.success("✅ Correct!")

            else:

                st.error(
                    f"❌ Wrong! Correct answer: {q['answer']}"
                )

            st.info(q["explanation"])

            st.rerun()

    else:

        if answer == q["answer"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Correct answer: {q['answer']}")

        st.info(q["explanation"])

        if st.button("Next Question"):

            st.session_state.current_question += 1
            st.session_state.answered = False

            st.rerun()