from flask import Flask, request, jsonify
import uuid
import requests
import logging
import os

app = Flask(__name__)

logging.basicConfig(
    filename='booking.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

@app.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    user = data.get("user")
    destination = data.get("destination")

    if not user or not destination:
        return jsonify({"error": "Missing user or destination"}), 400

    booking_id = str(uuid.uuid4())
    logging.info(f"Booking created: {booking_id} for {user} → {destination}")


    try:
        response = requests.post("http://notification-service:5002/notify/email", json={
            "user": user,
            "message": f"Your booking to {destination} is confirmed."
        })
        response.raise_for_status()
    except Exception as e:
        logging.error(f"Notification failed for booking {booking_id}: {e}")

    return jsonify({
        "booking_id": booking_id,
        "message": f"Booking confirmed for {user} to {destination}"
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
