from flask import Flask, request, jsonify
import uuid
import requests
import logging

app = Flask(__name__)
bookings = {}

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

@app.route("/bookings", methods=["POST"])
def create_booking():
    data = request.get_json()
    user = data.get("user")
    destination = data.get("destination")
    logging.info(f"Booking creation attempt - user: {user}, destination: {destination}")

    booking_id = str(uuid.uuid4())
    bookings[booking_id] = {
        "id": booking_id,
        "user": user,
        "destination": destination,
        "status": "confirmed pedram! You are Going!"
    }

    try:
        res = requests.post("http://notification-service:5002/notify/email", json={
            "user": user,
            "message": f"Booking confirmed for {destination}"
        })
        logging.info(f"Notification sent for booking {booking_id}, response: {res.status_code}")
    except Exception as e:
        logging.error(f"Notification failed for booking {booking_id}: {e}")

    return jsonify(bookings[booking_id]), 201

@app.route("/bookings/<booking_id>", methods=["GET"])
def get_booking(booking_id):
    logging.info(f"Booking lookup - id: {booking_id}")
    booking = bookings.get(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    return jsonify(booking), 200

@app.route("/bookings/<booking_id>", methods=["PATCH"])
def update_booking(booking_id):
    data = request.get_json()
    booking = bookings.get(booking_id)
    logging.info(f"Booking update attempt - id: {booking_id}, data: {data}")
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    if "status" in data:
        booking["status"] = data["status"]
        logging.info(f"Booking status updated - id: {booking_id}, new status: {data['status']}")
    return jsonify(booking), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
