import streamlit as st
from utils.pdf_export import create_summary_pdf


def show_summary_tab(text, summarize_text):

    st.subheader("📄 AI Summary")

    st.write(
        "Generate a concise study summary from the uploaded lecture."
    )

    # Keep the generated summary between Streamlit reruns
    if "summary" not in st.session_state:
        st.session_state.summary = None

    if st.button(
        "Generate AI Summary",
        key="summary_button"
    ):

        with st.spinner("Generating summary..."):

            st.session_state.summary = summarize_text(text)

    # Show the summary if it exists
    if st.session_state.summary:

        st.markdown(st.session_state.summary)

        # TXT Download
        st.download_button(
            label="⬇ Download Summary (.txt)",
            data=st.session_state.summary,
            file_name="SmartStudy_AI_Summary.txt",
            mime="text/plain"
        )

        # PDF Download
        pdf_file = create_summary_pdf(
            st.session_state.summary
        )

        st.download_button(
            label="⬇ Download Summary (.pdf)",
            data=pdf_file,
            file_name="SmartStudy_AI_Summary.pdf",
            mime="application/pdf"
        )