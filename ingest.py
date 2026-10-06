import os
from pathlib import Path
from pypdf import PdfReader
import json

folder_path = Path("data")
data=[]
for file in folder_path.glob("*.pdf"):
    print(f"-----Reading file------{file.name}")
    reader = PdfReader(file)
    print(f"no of pages{len(reader.pages)}")
    for page_no in range(len(reader.pages)):
        print(f"processing page: {page_no+1}")
        pdf_page = reader.pages[page_no]
        text=pdf_page.extract_text() #wrap this inside a option
        data.append({
            "file_name":f"{file.name}",
            "page_no":f"{page_no+1}",
            "text":f"{text}"
            
        })
    print(f"\n")
output_file=Path("output_data/output.json")
with open(output_file,"w") as f:
    json.dump(data,f,indent=4)
    