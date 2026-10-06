import json
import chromadb


# ============================================
# 1. Connect to local persistent ChromaDB
# ============================================

client = chromadb.PersistentClient(
    path="./chroma_db"
)


# ============================================
# 2. Create / get collection
# ============================================

collection = client.get_or_create_collection(
    name="rag"
)


# ============================================
# 3. Load your centralized JSON
# ============================================

json_file = "output_data/output.json"

with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)


# ============================================
# 4. Prepare data for ChromaDB
# ============================================

ids = []
documents = []
embeddings = []
metadatas = []


for page in data:

    file_name = page["file_name"]
    page_no = page["page_no"]

    for chunk in page["chunk"]:

        chunk_id = chunk["chunk_id"]
        text = chunk["text"]
        embedding = chunk["embedding"]

        # Create a unique ID for every chunk
        document_id = (
            f"{file_name}_page_{page_no}_chunk_{chunk_id}"
        )

        ids.append(document_id)

        documents.append(text)

        embeddings.append(embedding)

        metadatas.append({
            "file_name": file_name,
            "page_no": str(page_no),
            "chunk_id": str(chunk_id)
        })


# ============================================
# 5. Store embeddings in ChromaDB
# ============================================

if ids:

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )


# ============================================
# 6. Verify
# ============================================

print("Successfully stored embeddings in ChromaDB!")

print(f"Total chunks stored: {collection.count()}")

print("Database location: ./chroma_db")