from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# YOUR REAL 64-CHAR SERPAPI KEY HERE
SERPAPI_KEY = "077c0d0b55199e6970ab03d6c178784196797088bed46bb6d9de848c0c2405d7"   # ← PASTE YOUR FULL KEY

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
        r = requests.get("https://serpapi.com/search", params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
        for i, result in enumerate(data.get("organic_results", []), 1):
            if "ranklabel" in result.get("link", "").lower():
                return str(i)
        return ">10"
    except:
        return ">10"

@app.route('/', methods=['GET', 'POST'])
@app.route('/track', methods=['POST'])
def track():
    if request.method == 'GET':
        return "RankLabel API live"
    data = request.get_json() or {}
    keyword = data.get('keyword', '').strip()
    if not keyword:
        return jsonify({"error": "no keyword"}), 400
    rank = get_rank(keyword, SERPAPI_KEY)
    return jsonify({"keyword": keyword, "rank": rank})

# REQUIRED FOR VERCEL
from mangum import Mangum
handler = Mangum(app)
