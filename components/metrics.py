import streamlit as st


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