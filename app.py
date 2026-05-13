from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("BRAK OPENAI_API_KEY W .env")
else:
    print("Klucz API wykryty.")

client = OpenAI(api_key=api_key)

@app.route("/")
def home():
    return "MAJKAR AI Backend działa."

@app.route("/api/test", methods=["GET"])
def test():
    return jsonify({
        "status": "OK",
        "message": "Backend działa poprawnie"
    })

@app.route("/api/ai-mechanic", methods=["POST"])
def ai_mechanic():
    try:
        data = request.get_json(silent=True) or {}
        question = data.get("question", "").strip()

        if not question:
            return jsonify({"error": "Brak pytania"}), 400

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Jesteś AI Mechanikiem MAJKAR BOOK. Odpowiadasz po polsku, konkretnie, jak diagnosta samochodowy."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.choices[0].message.content

        return jsonify({"answer": answer})

    except Exception as e:
        print("DOKŁADNY BŁĄD:", str(e))
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)