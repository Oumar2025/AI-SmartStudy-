import streamlit as st


def setup_page():
    st.set_page_config(
        page_title="SmartStudy AI",
        page_icon="📚",
        layout="wide"
    )


def show_header():
    st.title("📚 SmartStudy AI")
    st.subheader("Intelligent Learning Assistant")

    st.write(
        "Upload your lecture PDF and let AI help you study smarter."
    )


def show_sidebar():

    with st.sidebar:

        st.title("📚 SmartStudy AI")

        st.markdown("---")

        st.subheader("Project Features")

        st.success("PDF Upload")
        st.success("AI Summary")
        st.success("Question Answering")
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

def show_document_info(character_count, chunk_count):

    st.subheader("📊 Document Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Characters",
            f"{character_count:,}"
        )

    with col2:
        st.metric(
            "Chunks",
            chunk_count
        )

    with col3:
        st.metric(
            "Knowledge Base",
            "Ready ✅"
        )

    st.divider()        