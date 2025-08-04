from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
logging.basicConfig(filename='log.txt', level=logging.INFO)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), nullable=False)
    item = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/order", methods=["POST"])
def place_order():
    data = request.get_json()
    user = data.get("user")
    item = data.get("item")
    if not user or not item:
        return jsonify({"error": "Missing user or item"}), 400
    order = Order(user=user, item=item)
    db.session.add(order)
    db.session.commit()
    logging.info(f"Order placed - user: {user}, item: {item}")
    return jsonify({"message": "Order placed", "order": {"user": user, "item": item}}), 201

@app.route("/orders", methods=["GET"])
def list_orders():
    all_orders = Order.query.all()
    results = [{"user": o.user, "item": o.item} for o in all_orders]
    return jsonify(results), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
