import chromadb

from embedding import generate_embedding


# ============================================
# 1. Connect to existing ChromaDB
# ============================================

client = chromadb.PersistentClient(
    path="./chroma_db"
)


# ============================================
# 2. Get your collection
# ============================================

collection = client.get_collection(
    name="rag"
)


# ============================================
# 3. User query
# ============================================

query = "What is Data augmentation (DA)?"


# ============================================
# 4. Generate embedding for the query
# ============================================

query_embedding = generate_embedding(query)


# ============================================
# 5. Search ChromaDB
# ============================================

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)


# ============================================
# 6. Display retrieved chunks
# ============================================

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for i in range(len(documents)):

    print("\n==============================")
    print(f"Result {i + 1}")
    print("==============================")

    print("Distance:", distances[i])

    print("Source:")
    print("File:", metadatas[i]["file_name"])
    print("Page:", metadatas[i]["page_no"])
    print("Chunk:", metadatas[i]["chunk_id"])

    print("\nText:")
    print(documents[i])