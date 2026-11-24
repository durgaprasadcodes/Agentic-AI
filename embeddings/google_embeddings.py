from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001", output_dimensionality=512, api_key=GEMINI_API_KEY
)

text = "I love learning Python and Machine Learning"

# Generate embedding
vector = embeddings.embed_query(text)

print("Embedding:", vector)
print("Dimensions:", len(vector))
