from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Fintech DevOps Demo API is running",
        "status": "healthy"
    })


@app.route("/transaction", methods=["POST"])
def transaction():
    data = request.get_json()

    if not data or "amount" not in data:
        return jsonify({
            "error": "Transaction amount is required"
        }), 400

    amount = data["amount"]

    if amount <= 0:
        return jsonify({
            "error": "Amount must be greater than zero"
        }), 400

    return jsonify({
        "message": "Transaction processed successfully",
        "amount": amount,
        "status": "success"
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)