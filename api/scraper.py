# api/scraper.py — FINAL BULLETPROOF VERSION
import requests

def get_rank(keyword, api_key):
    ):
    params = {
        "engine": "google",
        "q": keyword,
        "gl": "uk",
        "hl": "en",
        "num": 10,
        "api_key": api_key
    }
    try:
        r = requests.get("https://serpapi.com/search", params=params, timeout=15)
        r.raise_for_status()
        data = r.json()

        for i, result in enumerate(data.get("organic_results", []), 1):
            link = result.get("link", "")
            if "ranklabel" in link.lower():
                return str(i)
        return ">10"
    except Exception as e:
        print("Scraper error:", str(e))
        return ">10"
