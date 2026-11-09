import chromadb
from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Create a collection
collection = client.get_or_create_collection(
    name="electricity_tariff"
)

# Read the chunks
with open("chunks.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Separate individual chunks
chunks = [
    chunk.strip()
    for chunk in text.split("--- CHUNK")
    if chunk.strip()
]

# Generate embeddings and store them
for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk).tolist()

    collection.upsert(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[embedding]
    )

print("Total chunks stored:", len(chunks))
print("Electricity data successfully stored in ChromaDB!")