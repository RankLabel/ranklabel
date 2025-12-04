from flask import Flask, request, jsonify
from flask_cors import CORS  # ← This fixes the Carrd button
from scraper import get_rank
import os

app = Flask(__name__)
CORS(app)                    # ← Allows your Carrd site to call the API

# ←←←←← PUT YOUR REAL SERPAPI KEY HERE ←←←←←
SERPAPI_KEY = "YOUR_REAL_KEY_HERE"


def get_rank_with_key(keyword):
    return get_rank(keyword, SERPAPI_KEY)


# Main endpoint — this works both with and without /api
@app.route('/track', methods=['POST'])
@app.route('/api/track', methods=['POST'])
def track():
    data = request.json
    keyword = data.get('keyword', '').strip()
    if not keyword:
        return jsonify({"error": "Missing keyword"}), 400
    rank = get_rank_with_key(keyword)
    return jsonify({"keyword": keyword, "rank": rank})


# Home page — nice for testing
@app.route('/')
def home():
    return "RankLabel API — POST to /track with {'keyword': 'your keyword'}"


# Required for Vercel
if __name__ == "__main__":
    app.run()
