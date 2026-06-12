
import requests
import json

url = "http://127.0.0.1:8000/chat"
data = {"query": "How many products do we have?"}
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
