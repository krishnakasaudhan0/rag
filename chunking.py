from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import json 
from embedding import generate_embedding
import time 

file_path=("output_data/output.json")

if os.path.exists(file_path) and os.path.getsize(file_path)>0:
    with open(file_path,"r") as f:
        data=json.load(f)
else:
    print(f"file not found \n try to run ingest file ")
    exit()


def save_data():
    """Save current progress to JSON."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)



for page in data:
    print(f"processing page {page["page_no"]}")
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " "]
    )
    page_chunks = text_splitter.split_text(page["text"])

    page["chunk"] = []

    for i, chunk in enumerate(page_chunks): 
        page["chunk"].append({
            "chunk_id": i,
            "text": chunk,
            "embedding":generate_embedding(chunk)
        })
        save_data()
        print(f"processed page {page['page_no']} and saved")
        time.sleep(5)
        


