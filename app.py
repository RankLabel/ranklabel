from flask import Flask, request, jsonify
import scraper

app = Flask(__name__)

@app.route('/track', methods=['POST'])
def track():
    data = request.json
    keyword = data.get('keyword', '').strip()
    if not keyword:
        return jsonify({"error": "Missing keyword"}), 400
    rank = scraper.get_rank(keyword)
    return jsonify({"keyword": keyword, "rank": rank})

@app.route('/')
def home():
    return "RankLabel API — POST to /track"

if __name__ == "__main__":
    app.run(debug=True)
