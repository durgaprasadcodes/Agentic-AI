from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


sentences = text = "I love learning Python and Machine Learning"

embeddings = model.encode(sentences)

print("Text:", sentences)
print("Dimensions:", len(embeddings))
print("Embedding:", embeddings)
