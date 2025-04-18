from retriever.retriever import fetch_wikipedia_summary, fetch_news_snippets
from utils.keywords import extract_keywords
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import os

# Use Groq LLM (Mixtral) and fetch API key from Render env variable
llm = ChatGroq(
    model_name="mixtral-8x7b-32768",
    temperature=0.2,
    api_key=os.environ["GROQ_API_KEY"]
)

# Smart fact-checking prompt
prompt = PromptTemplate.from_template("""
You are a fact-checking expert. Given a CLAIM and supporting CONTEXT, analyze whether the context supports the claim.
Respond strictly in this format:
VERDICT: TRUE / FALSE / UNCERTAIN
EXPLANATION: <short reasoning>
CLAIM: {claim}
CONTEXT: {context}
""")

def get_fact_check_response(claim):
    keywords = extract_keywords(claim)
    wiki_data = fetch_wikipedia_summary(keywords[0])
    news_data, news_links = fetch_news_snippets(keywords)
    combined_context = f"Wikipedia Summary:\n{wiki_data}\n\nNews Snippets:\n{' '.join(news_data)}"

    # Run LLM pipeline
    full_prompt = prompt | llm
    result = full_prompt.invoke({"claim": claim, "context": combined_context})

    # Extract VERDICT and EXPLANATION
    verdict = "UNCERTAIN"
    explanation = result
    if "VERDICT:" in result:
        parts = result.split("VERDICT:")[1].split("EXPLANATION:")
        verdict = parts[0].strip().upper()
        explanation = parts[1].strip() if len(parts) > 1 else explanation

    confidence = 90 if verdict == "TRUE" else 50 if verdict == "UNCERTAIN" else 30
    sources = ["https://en.wikipedia.org/wiki/" + keywords[0].replace(' ', '_')] + news_links

    return {
        "verdict": verdict,
        "explanation": explanation,
        "sources": sources,
        "confidence": confidence
    }
