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

def generate_quiz(text):

    prompt = f"""
You are SmartStudy AI.

Create a study quiz from the lecture notes below.

Rules:

- Create exactly 5 multiple-choice questions.
- Each question must have 4 options (A, B, C, D).
- Clearly indicate the correct answer.
- Add a one-sentence explanation after each answer.
- Format the quiz neatly using Markdown.

Lecture Notes:

{text[:6000]}
"""

    return llm.invoke(prompt)