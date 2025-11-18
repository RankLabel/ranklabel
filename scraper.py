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
        results = response.json().get("organic_results", [])
        for i, result in enumerate(results):
            if "ranklabel.co.uk" in result.get("link", ""):
                return i + 1
        return ">10"
    except:
        return "Error"

# REMOVE THE TEST PART BELOW (or comment it out)
# if __name__ == "__main__":
#     API_KEY = "077c0d0b55199e6970ab03d6c178784196797088bed46bb6d9de848c0c2405d7"
#     print(get_rank("seo agency london", API_KEY))
