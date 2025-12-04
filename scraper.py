# api/scraper.py — BULLET-PROOF VERSION
import requests

def get_rank(keyword, api_key):
    params = {
        "engine": "google",
        "q": keyword,
        "gl": "uk",
        "hl": "en",
        "num": 10,
        "api_key": api_key
    }
    try:
        response = requests.get("https://serpapi.com/search", params=params, timeout=10)
        response.raise_for_status()  # Raises error for bad status
        data = response.json()
        
        if "organic_results" not in data or not data["organic_results"]:
            return ">10"
        
        for i, result in enumerate(data["organic_results"], 1):
            link = result.get("link", "")
            if "ranklabel.co.uk" in link or "ranklabel.carrd.co" in link:
                return str(i)
        
        return ">10"
    except requests.exceptions.RequestException as e:
        print(f"SerpApi request error: {e}")
        return ">10"
    except Exception as e:
        print(f"Scraper error: {e}")
        return ">10"
