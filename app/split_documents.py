from load_documents import documents
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

# Split documents
chunks = text_splitter.split_documents(documents)

print("Documents split successfully!")
print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk.page_content)