import streamlit as st
from utils.vector_store import create_vector_store, search_document
from utils.chatbot import summarize_text, answer_question

from utils.pdf_reader import extract_text_from_pdf
from utils.embeddings import split_text
from utils.vector_store import create_vector_store
from utils.chatbot import summarize_text

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="SmartStudy AI",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("📚 SmartStudy AI")
st.subheader("Intelligent Learning Assistant")

st.write(
    "Upload your lecture PDF and let AI help you study smarter."
)

# -----------------------------
# PDF UPLOAD
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a Lecture PDF",
    type="pdf"
)

# -----------------------------
# READ PDF
# -----------------------------
if uploaded_file is not None:

    text = extract_text_from_pdf(uploaded_file)

    st.success("✅ PDF uploaded successfully!")

    st.subheader("Preview")

    st.text_area(
        "Extracted Text",
        text[:3000],
        height=350
    )

    st.info(f"Characters extracted: {len(text)}")
    chunks = split_text(text)

    st.success(f"Document split into {len(chunks)} chunks.")
    vector_store = create_vector_store(chunks)

    st.success("Knowledge base created successfully!")
    st.info(f"Knowledge base contains {len(chunks)} document chunks.")

    with st.expander("View Chunks"):

        for i, chunk in enumerate(chunks[:5]):
            st.markdown(f"### Chunk {i+1}")
            st.write(chunk)
    st.divider()
    st.divider()

    st.subheader("Ask Questions")

    question = st.text_input(
        "Ask anything about the uploaded PDF"
    )

    if st.button("Get Answer"):

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

    if st.button("Generate AI Summary"):

        with st.spinner("AI is reading your lecture..."):

            summary = summarize_text(text)

        st.subheader("AI Summary")

        st.write(summary)