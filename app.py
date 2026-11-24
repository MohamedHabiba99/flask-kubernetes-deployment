import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        message=os.environ.get("APP_MESSAGE", "Hello from my CI/CD pipeline!"),
        environment=os.environ.get("APP_ENV", "local"),
        pod=os.environ.get("HOSTNAME", "unknown"),
        version="2.0",
    )

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)