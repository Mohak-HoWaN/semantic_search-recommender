import os
from flask import Flask, request, jsonify
import numpy as np
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load the transformer model once at startup
model = SentenceTransformer('all-MiniLM-L6-v2')  # You can use other models if you want

def get_embedding(text):
    return model.encode(text).tolist()

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

@app.route('/semantic-search', methods=['POST'])
def semantic_search():
    try:
        data = request.json
        query = data["query"]
        questions = data["questions"]  # [{id, title, description}]
        query_emb = get_embedding(query)
        results = []
        for q in questions:
            q_emb = get_embedding(q["title"] + " " + q["description"])
            score = cosine_similarity(query_emb, q_emb)
            q["score"] = score
            results.append(q)
        results.sort(key=lambda x: x["score"], reverse=True)
        return jsonify({"results": results[:5]})
    except Exception as e:
        print("Error in /semantic-search:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        user_tags = set(data["userTags"])
        questions = data["questions"]
        recommended = [q for q in questions if user_tags.intersection(set(q["tags"]))]
        return jsonify({"recommended": recommended[:10]})
    except Exception as e:
        print("Error in /recommend:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
