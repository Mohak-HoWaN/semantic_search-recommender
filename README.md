# 🔍 Semantic Q&A Platform – Flask + Next.js

This project integrates a **Flask** backend for semantic search and recommendations with a **Next.js** frontend for a dynamic and responsive user interface.

---

## 📁 Project Structure

```
/flask-backend/       # Flask API (app.py, requirements.txt, etc.)
/nextjs-frontend/     # Next.js app (React UI, pages, components, etc.)
```

---

## 🚀 Setup Instructions

### 🔧 Flask Backend Setup

1. **Navigate to the backend folder:**
   ```bash
   cd flask-backend
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server:**
   ```bash
   python app.py
   ```

> Server runs at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔗 Connecting Next.js to Flask

### 1. API Requests from Next.js

Use `fetch` or `axios` to send requests to Flask endpoints:

```js
const res = await fetch('http://127.0.0.1:5000/semantic-search', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ query, questions }),
});
const data = await res.json();
```

### 2. Optional: Development Proxy

To avoid CORS issues during development, add a proxy in `next.config.js`:

```js
// next.config.js
module.exports = {
  async rewrites() {
    return [
      {
        source: '/api/flask/:path*',
        destination: 'http://127.0.0.1:5000/:path*',
      },
    ];
  },
};
```

Now, you can call Flask routes like:

```js
fetch('/api/flask/semantic-search', { ... });
```

---

## 🧠 Flask API Endpoints

### `POST /semantic-search`

**Request:**

```json
{
  "query": "Your search string",
  "questions": [
    { "id": 1, "title": "...", "description": "...", "tags": ["..."] }
  ]
}
```

**Response:**

```json
{
  "results": [
    { "id": 2, "title": "...", "score": 0.37, ... }
  ]
}
```

---

### `POST /recommend`

**Request:**

```json
{
  "userTags": ["tag1", "tag2"],
  "questions": [
    { "id": 1, "title": "...", "description": "...", "tags": ["..."] }
  ]
}
```

**Response:**

```json
{
  "recommended": [
    { "id": 1, "title": "...", ... }
  ]
}
```

---

## 🛠️ Integration Guide

- **Backend logic**: Handle semantic search & recommendations in Flask.
- **Frontend API calls**: Place logic in:
  - `getServerSideProps` / `getStaticProps`
  - `/pages/api/` routes
  - React components via `fetch`/`axios`
- **UI Components**: Render results in your Q&A interface.

---

## 📦 Deployment Notes

- Make sure the Flask backend is running for Next.js to access AI endpoints.
- For production:
  - Host Flask via a microservice or serverless function.
  - Vercel supports Python for serverless deployment.
- For local development:
  - Use a proxy (`next.config.js`) or manage CORS headers in Flask.

---

## 📚 References

- [Next.js + Flask Integration Guide](https://vercel.com/docs)
- [Example Next.js + Flask Repo](https://github.com/search?q=nextjs+flask)
- [Semantic Search Concepts](https://huggingface.co/blog/semantic-search)
