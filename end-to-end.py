import requests

# register
res1 = requests.post("http://localhost:5000/register", json={"username": "mary", "password": "password"})
print("Registered succesfuly:", res1.status_code, res1.json())

# make a booking
res2 = requests.post("http://localhost:5001/bookings", json={"user": "mary", "destination": "tehran"})
print("Booking confirmation for flight:", res2.status_code, res2.json())
