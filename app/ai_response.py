
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

from role_retriever import retrieve_documents

# Load API key from .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

client = Groq()


def generate_answer(question, role):
    # Retrieve relevant documents based on the user's role
    documents = retrieve_documents(question, role)

    # Combine retrieved text into context
    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    # Generate answer using Groq
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
    "You are an AI Clinical App assistant that answers questions using retrieved clinic documents.\n\n"
    "STRICT RULES:\n"
    "1. Use ONLY the information explicitly stated in the provided context.\n"
    "2. Do not use your own medical knowledge or outside knowledge to fill gaps.\n"
    "3. Do not invent clinic features, policies, procedures, statistics, services, or instructions.\n"
    "4. Do not assume a feature exists just because it is common in other clinics.\n"
    "5. If the context only partially answers the question, provide only supported information and clearly state what is missing.\n"
    "6. If the context does not contain the answer, say: 'I cannot find this information in the available clinic documents.'\n"
    "7. Do not make medical diagnoses, prescribe treatment, or invent medical advice.\n"
    "8. Respect the user's role and answer only using the context retrieved for that role.\n"
    "9. Keep answers clear, concise, and factual.\n\n"
    "Your answer must be supported by the provided context."
)
            },
            {
                "role": "user",
                "content": (
                    f"User role: {role}\n\n"
                    f"Context:\n{context}\n\n"
                    f"Question: {question}"
                )
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


# Test the AI response
if __name__ == "__main__":
    question = "How can I create staff accounts and change user access permissions?"
    role = "patient"

    answer = generate_answer(question, role)

    print("\n--- AI CLINICAL APP RESPONSE ---")
    print(answer)
