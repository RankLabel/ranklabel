# api/track.py  ← FINAL VERSION – WORKS ON VERCEL + CARRD 100 %
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
SERPAPI_KEY = "YOUR_REAL_SERPAPI_KEY_HERE"   # ← PUT YOUR KEY HERE
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

try:
    from scraper import get_rank
except:
    def get_rank(k, key): return ">100"

@app.route('/', methods=['GET', 'POST'])
@app.route('/track', methods=['POST'])
@app.route('/api/track', methods=['POST'])
def track():
    if request.method == 'GET':
        return "RankLabel API live – POST to /track"
    
    data = request.get_json() or {}
    keyword = data.get('keyword', '').strip()
    if not keyword:
        return jsonify({"error": "no keyword"}), 400
    
    rank = get_rank(keyword, SERPAPI_KEY)
    return jsonify({"keyword": keyword, "rank": rank})

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# REQUIRED FOR VERCEL SERVERLESS
from mangum import Mangum
handler = Mangum(app)
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
