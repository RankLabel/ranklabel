from flask import Flask, request, jsonify
from scraper import get_rank  # ← This loads your scraper.py
import os

app = Flask(__name__)

# ←←← YOUR SERPAPI KEY HERE ←←←
SERPAPI_KEY = "077c0d0b55199e6970ab03d6c178784196797088bed46bb6d9de848c0c2405d7"

# Pass key to scraper
def get_rank_with_key(keyword):
    return get_rank(keyword, SERPAPI_KEY)

@app.route('/track', methods=['POST'])
def track():
    data = request.json
    keyword = data.get('keyword', '').strip()
    if not keyword:
        return jsonify({"error": "Missing keyword"}), 400
    rank = get_rank_with_key(keyword)
    return jsonify({"keyword": keyword, "rank": rank})

@app.route('/')
def home():
    return "RankLabel API — POST to /track with {'keyword': 'your keyword'}"

if __name__ == '__main__':
    app.run(debug=True)
