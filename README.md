
# 🔍 AI Fact Checker using RAG (Live Mode)

This project uses **Retrieval-Augmented Generation (RAG)** to verify claims by pulling **live data** from Wikipedia and news APIs.

## 🚀 Features
- Real-time fact-checking using current data
- Wikipedia + NewsAPI integration
- Streamlit UI with verdict, summary, sources & confidence

## 🖥 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🐳 Docker Deployment

```bash
docker build -t fact-checker-live .
docker run -p 8501:8501 fact-checker-live
```

## 🌐 Render Deployment

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `streamlit run app.py --server.port=10000 --server.address=0.0.0.0`

---

**Built by LP and VR**
