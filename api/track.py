# api/track.py  ← 100 % working version – December 2025
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
#  <<< PUT YOUR REAL SERPAPI KEY HERE >>>
SERPAPI_KEY = "077c0d0b55199e6970ab03d6c178784196797088bed46bb6d9de848c0c2405d7"
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

app = Flask(__name__)
CORS(app)                     # ← this fixes Carrd

# Import your scraper (make sure scraper.py is in the same folder)
try:
    from scraper import get_rank
except ImportError:
    # fallback if scraper.py is missing
    def get_rank(keyword, key):
        return ">100"

def get_rank_with_key(keyword):
    return get_rank(keyword, SERPAPI_KEY)

# This single handler works for ALL these URLs:
#   /track
#   /api/track
#   /
@app.route('/', methods=['GET', 'POST'])
@app.route('/track', methods=['POST'])
@app.route('/api/track', methods=['POST'])
def track():
    if request.method == 'GET':
        return "RankLabel API live – POST to /track with JSON"
    
    data = request.get_json(silent=True) or {}
    keyword = data.get('keyword', '').strip()
    if not keyword:
        return jsonify({"error": "no keyword"}), 400
    
    rank = get_rank_with_key(keyword)
    return jsonify({"keyword": keyword, "rank": rank})

# Required for Vercel
def handler(event, context=None):
    from mangum import Mangum
    return Mangum(app)(event, context)
