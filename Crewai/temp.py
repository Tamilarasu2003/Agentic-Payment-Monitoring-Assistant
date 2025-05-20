import requests

url = "http://localhost:8000/run-agents"
file_path = "./payment_transactions.csv"

with open(file_path, "rb") as f:
    files = {"file": (file_path, f, "text/csv")}
    response = requests.post(url, files=files)

if response.headers.get("Content-Type") == "application/json":
    print(response.json())
else:
    print("Response is not JSON:", response.text)