from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2:3b"
)


def summarize_text(text):
    prompt = f"""
You are an intelligent study assistant.

Summarize the following lecture notes into clear and concise study notes.

Lecture:

{text[:6000]}
"""

    return llm.invoke(prompt)


def answer_question(question, context):

    prompt = f"""
You are an intelligent study assistant.

Answer ONLY using the information provided below.

If the answer is not in the document, say:

"I couldn't find the answer in the uploaded document."

Document:

{context}

Question:

{question}

Answer:
"""

    return llm.invoke(prompt)