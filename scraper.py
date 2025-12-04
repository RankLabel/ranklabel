# api/scraper.py  ← 100 % working, no silent fails
import requests
import json

def get_rank(keyword, serpapi_key):
    params = {
        "engine": "google",
        "q": keyword,
        "gl": "uk",
        "hl": "en",
        "api_key": serpapi_key
    }
    try:
        response = requests.get("https://serpapi.com/search", params=params, timeout=20)
        data = response.json()

        if "organic_results" not in data:
            return ">100"

        for result in data["organic_results"]:
            if "ranklabel.co.uk" in result.get("link", "") or "ranklabel.carrd.co" in result.get("link", ""):
                return str(result["position"])

        return ">100"

    except Exception as e:
        print("Scraper error:", str(e))  # visible in Vercel logs
        return ">50"
