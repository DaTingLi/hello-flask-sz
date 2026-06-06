"""hello-flask-sz: A minimal Flask web service for CI/CD demonstration."""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def welcome():
    """Return a welcome message in JSON format."""
    return jsonify({"message": "Welcome to hello-flask-sz"}), 200


@app.route("/health")
def health():
    """Health check endpoint for deployment verification."""
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)
