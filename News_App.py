import requests
import json
import os

# Secure API key storage (Use environment variables)
API_KEY = os.getenv("NEWS_API_KEY") 

if not API_KEY:
    print("Error: API Key not found. Set NEWS_API_KEY as an environment variable.")
    exit()

query = input("What type of news are you interested in? ")

url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"

try:
    r = requests.get(url)
    r.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
    news = r.json()

    if "articles" in news:
        for article in news["articles"][:10]:  # Show only the top 10 results
            print(article["title"])
            print(article["description"] if article["description"] else "No description available.")
            print("--------------------------------------")
    else:
        print("No articles found.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching news: {e}")

    print("--------------------------------------")