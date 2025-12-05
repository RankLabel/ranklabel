from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allows Carrd

# YOUR 64-CHAR SERPAPI KEY
SERPAPI_KEY = "077c0d0b55199e6970ab03d6c178784196797088bed46bb6d9de848c0c2405d7"

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
    except Exception as e:
        print(f"Error: {e}")
        return ">10"

@app.route('/', methods=['GET'])
def home():
    return "RankLabel API live – POST to /api/track"

@app.route('/api/track', methods=['POST'])
def track():
    data = request.get_json() or {}
    keyword = data.get('keyword', '').strip()
    if not keyword:
        return jsonify({"error": "No keyword"}), 400
    rank = get_rank(keyword, SERPAPI_KEY)
    return jsonify({"keyword": keyword, "rank": rank})

from mangum import Mangum
handler = Mangum(app)
