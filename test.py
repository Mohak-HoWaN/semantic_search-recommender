import requests

BASE = "http://localhost:5000"

questions = [
    {"id": 1, "title": "How to use React?", "description": "I want to learn React basics.", "tags": ["react", "frontend"]},
    {"id": 2, "title": "JWT authentication", "description": "How does JWT work in APIs?", "tags": ["jwt", "security"]},
    {"id": 3, "title": "Python list comprehension", "description": "Examples of list comprehension in Python.", "tags": ["python", "basics"]},
]

def print_response(resp):
    print(f"Status Code: {resp.status_code}")
    try:
        print("JSON:", resp.json())
    except Exception as e:
        print("Raw Response:", resp.text)
        print("Error:", e)

# Test semantic search
resp = requests.post(f"{BASE}/semantic-search", json={
    "query": "How to secure my API?",
    "questions": questions
})
print("Semantic Search Results:")
print_response(resp)

# Test recommendations
resp = requests.post(f"{BASE}/recommend", json={
    "userTags": ["react", "security"],
    "questions": questions
})
print("\nRecommendations:")
print_response(resp)
