from pathlib import Path
from langchain_core.documents import Document

# Find the documents folder
project_folder = Path(__file__).resolve().parent.parent
documents_folder = project_folder / "documents"

documents = []

# Load all text files
for file_path in documents_folder.glob("*.txt"):
    text = file_path.read_text(encoding="utf-8")

    document = Document(
        page_content=text,
        metadata={"source": file_path.name}
    )

    documents.append(document)

print("Documents loaded successfully!")

for document in documents:
    print(f"\nFile: {document.metadata['source']}")
    print(f"Characters: {len(document.page_content)}")

print(f"\nTotal documents loaded: {len(documents)}")