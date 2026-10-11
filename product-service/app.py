
from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 45000, "stock": 10},
    {"id": 2, "name": "Headphones", "price": 2000, "stock": 25},
    {"id": 3, "name": "Keyboard", "price": 1500, "stock": 15}
]

@app.route("/")
def home():
    return jsonify({
        "service": "Product Service",
        "status": "running",
        "message": "Welcome to the Product API"
    })

@app.route("/products")
def get_products():
    return jsonify(products)

@app.route("/products/<int:product_id>")
def get_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
