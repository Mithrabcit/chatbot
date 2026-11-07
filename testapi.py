import requests

url = "http://127.0.0.1:8000/ask"

question = input("Enter your question: ")

data = {
    "question": question
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Answer:", response.json()["answer"])