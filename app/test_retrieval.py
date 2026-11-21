from role_retriever import retrieve_documents

question = "What should a patient do to manage their appointments?"
role = "patient"

print(f"\nTesting role: {role.upper()}")
print(f"Question: {question}")
print("=" * 60)

documents = retrieve_documents(question, role)

if not documents:
    print("No documents retrieved.")
else:
    for i, doc in enumerate(documents, start=1):
        print(f"\n--- Retrieved Chunk {i} ---")
        print("Source:", doc.metadata.get("source", "Unknown"))
        print("Content:")
        print(doc.page_content)
        print("-" * 60)