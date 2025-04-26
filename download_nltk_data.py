import nltk

def download_nltk_resources():
    nltk.download('punkt')    # Fixes tokenizer errors (e.g., punkt_tab)
    nltk.download('stopwords') # Required for stopwords filtering

if __name__ == "__main__":
    download_nltk_resources()
    print("✅ NLTK data downloaded successfully!")