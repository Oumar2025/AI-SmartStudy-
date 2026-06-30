from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text):
    """
    Split the text into overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_text(text)

    return chunks