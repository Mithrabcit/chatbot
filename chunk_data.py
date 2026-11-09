# Read the extracted PDF text

with open("electricity_data.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Set chunk size and overlap
chunk_size = 1000
overlap = 200

chunks = []

start = 0

while start < len(text):
    end = start + chunk_size

    chunk = text[start:end]

    chunks.append(chunk)

    start += chunk_size - overlap

# Display the number of chunks
print("Total chunks:", len(chunks))

# Save chunks into a text file
with open("chunks.txt", "w", encoding="utf-8") as file:
    for i, chunk in enumerate(chunks):
        file.write(f"\n--- CHUNK {i + 1} ---\n")
        file.write(chunk + "\n")

print("Text chunking completed successfully!")