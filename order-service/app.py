
from flask import Flask, jsonify

app = Flask(__name__)

orders = [
    {"id": 1001, "product": "Laptop", "quantity": 1, "status": "Shipped"},
    {"id": 1002, "product": "Headphones", "quantity": 2, "status": "Processing"}
]

@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "status": "running",
        "message": "Welcome to the Order API"
    })

@app.route("/orders")
def get_orders():
    return jsonify(orders)

@app.route("/orders/<int:order_id>")
def get_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            return jsonify(order)

    return jsonify({"error": "Order not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
