from flask import Flask, request, jsonify
import logging

# Logging configuration
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

app = Flask(__name__)

@app.route("/notify/email", methods=["POST"])
def send_email():
    data = request.get_json()
    user = data.get("user")
    message = data.get("message")

    if not user or not message:
        logging.warning("Notification failed: missing user or message")
        return jsonify({"error": "Missing user or message"}), 400
                           
    logging.info(f"Email sent to: {user}, message: {message}")
    print("📬 Notification Service Log:")
    print(f"    Email successfully sent to: {user}")
    print(f"    📩 Message content: {message}\n")
    
    return jsonify({"status": "email sent", "user": user}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
