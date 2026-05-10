# from sentence_transformers import SentenceTransformer


# model = SentenceTransformer(
#     "sentence-transformers/all-MiniLM-L6-v2"
# )

from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize client (replaces genai.configure())
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_embedding(text: str) -> list[float]:
    """
    Generate embedding using Gemini API (text-embedding-004).
    Output dimension: 768 (default), supports matryoshka up to 3072.
    """
    response = client.models.embed_content(
        model="gemini-embedding-2",
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT"
        )
    )
    return response.embeddings[0].values