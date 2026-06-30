import streamlit as st
from utils.ui import (
    setup_page,
    show_header,
    show_sidebar,
    show_document_info
)
from utils.vector_store import create_vector_store, search_document
from utils.chatbot import (
    summarize_text,
    answer_question,
    generate_quiz
)

from utils.pdf_reader import extract_text_from_pdf
from utils.embeddings import split_text
from utils.vector_store import create_vector_store
from utils.chatbot import summarize_text

setup_page()
show_sidebar()
show_header()

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

   
    chunks = split_text(text)

   
    vector_store = create_vector_store(chunks)
    show_document_info(
        len(text),
        len(chunks)
    )
    tab1, tab2, tab3 = st.tabs(
    [
        "📄 Summary",
        "💬 Ask Questions",
        "📝 Quiz Generator"
    ]
)

    
    

    with st.expander("View Chunks"):

        for i, chunk in enumerate(chunks[:5]):
            st.markdown(f"### Chunk {i+1}")
            st.write(chunk)
    st.divider()
    st.divider()

    with tab2:

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

    with tab3:

        st.subheader("📝 Quiz Generator")

        st.write(
            "Generate multiple-choice questions from the uploaded lecture."
        )

        if st.button("Generate Quiz"):

            with st.spinner("Generating quiz..."):

                quiz = generate_quiz(text)

            st.markdown(quiz)     

    with tab1:

        if st.button("Generate AI Summary"):

            with st.spinner("AI is reading your lecture..."):

                summary = summarize_text(text)

            st.subheader("AI Summary")

            st.write(summary)
