from flask import Flask, request, jsonify
from google import genai
from google.genai import types

client=genai.Client(api_key="AIzaSyDOWCHR9NwLysKGGqHx82qx0ifGbSf5Pqk")

app = Flask(__name__)

@app.route("/")
def home():
    return "Ok"

@app.route("/chat", methods=["POST"])
def chat():
    return client.models.generate_content(
         model="gemini-2.0-flash",
         contents=request.json["msg"]
).text
app.run(port=5001)
        
if __name__ == "__main__":
    app.run(debug=True,  port=5001)