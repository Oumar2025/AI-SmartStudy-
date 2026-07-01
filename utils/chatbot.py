from langchain_ollama import OllamaLLM
import ast
import re

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

Generate exactly 5 multiple-choice questions.

Return ONLY JSON.

Example:

[
 {{
   "question":"...",
   "options": {{
      "A":"...",
      "B":"...",
      "C":"...",
      "D":"..."
   }},
   "answer":"A",
   "explanation":"..."
 }}
]

Lecture:

{text[:6000]}
"""

    response = llm.invoke(prompt)

    print("\n========== AI RESPONSE ==========\n")
    print(response)
    print("\n===============================\n")

    # Remove markdown if present
    response = response.replace("```json", "")
    response = response.replace("```", "")

    # Extract JSON array
    match = re.search(r"\[.*\]", response, re.DOTALL)

    if match:

        json_text = match.group(0)

        try:
            return ast.literal_eval(json_text)

        except Exception as e:

            print("Quiz parsing error:", e)
            return []