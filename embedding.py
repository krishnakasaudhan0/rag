from google import genai
from google.genai import types  # <-- FIX: Changed this line
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the client
client = genai.Client(api_key=os.getenv("GOOGLE_GEMINI"))

def generate_embedding(chunk):
    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=chunk,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",
        ),
    )
    # The SDK returns a list of embedding objects; we grab the values array
    return result.embeddings[0].values


