
import re

def extract_keywords(text):
    words = re.findall(r'\b[A-Za-z]{4,}\b', text)
    return list(dict.fromkeys(words))[:3]
