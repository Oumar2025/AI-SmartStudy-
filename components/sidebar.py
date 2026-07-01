import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.title("📚 SmartStudy AI")

        st.markdown("---")

        st.subheader("Project Features")

        st.success("PDF Upload")
        st.success("AI Summary")
        st.success("Question Answering")
        st.success("Quiz Generator")
        st.success("RAG + FAISS")

        st.markdown("---")

        st.info(
            """
Model:
Llama 3.2

Embeddings:
MiniLM-L6-v2

Vector DB:
FAISS
"""
        )