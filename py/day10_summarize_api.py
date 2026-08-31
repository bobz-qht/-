import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from day4_summarizer import summarize_text

app = Flask(__name__)
CORS(app)


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "text가 없습니다"}), 400

    summary = summarize_text(text)
    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(port=5000)