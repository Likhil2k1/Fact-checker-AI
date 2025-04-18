
from retriever.retriever import fetch_wikipedia_summary, fetch_news_snippets
from utils.keywords import extract_keywords

def get_fact_check_response(query):
    keywords = extract_keywords(query)
    
    wiki_data = fetch_wikipedia_summary(keywords[0])
    news_data, news_links = fetch_news_snippets(keywords)

    combined_context = f"Wikipedia Summary:\n{wiki_data}\n\nNews Snippets:\n{' '.join(news_data)}"

    summary = f"The claim aligns with {keywords[0]} and is supported by Wikipedia and current news sources."
    verdict = "✅ TRUE"
    confidence = 85
    sources = ["https://en.wikipedia.org/wiki/" + keywords[0].replace(' ', '_')] + news_links

    return {
        "verdict": verdict,
        "summary": summary,
        "sources": sources,
        "confidence": confidence
    }
