
# 🧠 AI Fact Checker using RAG (Smart Mode)

This project combines live data retrieval and reasoning with an LLM to provide accurate fact-checking.

## 🚀 Features
- Real-time Wikipedia + NewsAPI retrieval
- Reasoning via Mistral using LangChain
- Structured verdicts: TRUE / FALSE / UNCERTAIN
- Confidence scores and source listing

## 🖥 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🐳 Docker Deployment

```bash
docker build -t fact-checker-smart .
docker run -p 8501:8501 fact-checker-smart
```

## 🌐 Deploy to Render

- Build: `pip install -r requirements.txt`
- Start: `streamlit run app.py --server.port=10000 --server.address=0.0.0.0`

---

**Built by LP and VR**
