from flask import Flask, request, jsonify
from flask_cors import CORS
from chat import get_response
from datetime import datetime
from datetime import date

app = Flask(__name__)
CORS(app)


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
#TODO:check if text is valid
    response = get_response(text)

    def simple(text):
        if text == "what time is it":
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
