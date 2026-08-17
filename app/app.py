from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Basic application logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


@app.route("/")
def home():
    logger.info("Home endpoint accessed")

    return jsonify({
        "message": "Fintech DevOps Demo API is running",
        "status": "healthy"
    })


@app.route("/health")
def health():
    logger.info("Health check requested")

    return jsonify({
        "application": "Fintech Demo",
        "status": "running"
    }), 200


@app.route("/transaction", methods=["POST"])
def transaction():
    data = request.get_json()

    if not data or "amount" not in data:
        logger.warning("Invalid transaction request: amount missing")

        return jsonify({
            "error": "Transaction amount is required"
        }), 400

    amount = data["amount"]

    if amount <= 0:
        logger.warning(
            f"Invalid transaction attempted with amount: {amount}"
        )

        return jsonify({
            "error": "Amount must be greater than zero"
        }), 400

    logger.info(
        f"Transaction processed successfully. Amount: {amount}"
    )

    return jsonify({
        "message": "Transaction processed successfully",
        "amount": amount,
        "status": "success"
    }), 201


@app.route("/transactions", methods=["GET"])
def get_transactions():
    logger.info("Transaction history requested")

    transactions = [
        {
            "id": 1,
            "amount": 1000,
            "status": "success"
        },
        {
            "id": 2,
            "amount": 2500,
            "status": "success"
        }
    ]

    return jsonify({
        "transactions": transactions,
        "count": len(transactions)
    })


if __name__ == "__main__":
    logger.info("Starting Fintech DevOps application")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )