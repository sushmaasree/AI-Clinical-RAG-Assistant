from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "chroma_db"

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load existing vector database
vector_db = Chroma(
    persist_directory=str(DB_PATH),
    embedding_function=embeddings
)

# Define document access for each role
ROLE_FILES = {
    "admin": ["general_clinic.txt", "admin_guide.txt"],
    "doctor": ["general_clinic.txt", "doctor_guide.txt"],
    "staff": ["general_clinic.txt", "staff_guide.txt"],
    "patient": ["general_clinic.txt", "patient_guide.txt"]
}

def retrieve_documents(question, role):
    role = role.lower()

    if role not in ROLE_FILES:
        raise ValueError("Invalid user role")

    results = vector_db.similarity_search(
        question,
        k=5,
        filter={"source": {"$in": ROLE_FILES[role]}}
    )

    return results


# Test retrieval
if __name__ == "__main__":
    question = "How can I manage appointments?"

    for role in ROLE_FILES:
        print(f"\n--- {role.upper()} RESULTS ---")

        results = retrieve_documents(question, role)

        for result in results:
            print("Source:", result.metadata["source"])
            print(result.page_content[:200])