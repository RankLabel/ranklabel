from flask import Flask, request, jsonify
from scraper import get_rank
import os

app = Flask(__name__)

# ←←←←← PUT YOUR REAL SERPAPI KEY HERE ←←←←←
SERPAPI_KEY = "YOUR_REAL_KEY_HERE"

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

# Vercel serverless export (required for routes)
app = app
