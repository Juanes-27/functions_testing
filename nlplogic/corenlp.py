from textblob import TextBlob
import wikipedia

def search_wikipedia(name):
    """Search Wikipedia pages"""
    
    print(f"Searching for name: {name}")
    search = wikipedia.search(name)
    return search

def summarize_wikipedia(name):
    """Summarize Wikipedia page"""
    
    print(f"Finding wikipedia summary for name {name}")
    summary = wikipedia.summary(name)
    return summary

def get_text_blob(text):
    """Gets text blob object and return"""
    blob = TextBlob(text)
    return blob

def get_phrases(name):
    """Find Wikipedia name and return back phrases"""
    
    text = summarize_wikipedia(name)
    blob = TextBlob(text)
    phrases = blob.noun_phrases
    return phrases
    
    
