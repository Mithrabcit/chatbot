import chromadb
from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to existing database
client = chromadb.PersistentClient(path="./chroma_db")

# Access electricity collection
collection = client.get_collection(
    name="electricity_tariff"
)

# Ask a sample question
question = "What are the electricity tariff rates for domestic consumers?"

# Convert question into embedding
question_embedding = model.encode(question).tolist()

# Search for relevant information
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)

# Display retrieved information
print("\nRelevant information:\n")

for document in results["documents"][0]:
    print(document)
    print("----------------------")