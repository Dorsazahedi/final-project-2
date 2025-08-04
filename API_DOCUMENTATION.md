
# API Documentation-Microservices and endpoints
## Integration Explaining:

When a new booking is made through the booking service it automatically sends a notification request to the notification service. The result of this interaction printed is in the Docker terminal logs, which has been documented in the pdf file.
## User Service ('5000`)

### POST `/register`
Registers a new user.

**Request body:**
```json
{
  "username": "pedram",
  "password": "1234"
}
```

**Response (201):**
```json
{
  "message": "User pedram registered successfully!congradulations!",
  "user_id": "uuid-string"
}
```

---

### POST `/login`
Authenticates a registered user.

**Request body:**
```json
{
  "username": "pedram",
  "password": "1234"
}
```

**Response (200):**
```json
{
  "message": "Welcome back, pedram!",
  "user_id": "uuid-string"
}
```

---

### GET `/profile/<user_id>`
Returns profile details for the specified user ID.

**Example response (200):**
```json
{
  "user_id": "uuid-string",
  "username": "alice"
}
```

---

## Booking Service (`5001`)

### POST `/bookings`
Creates a new booking .

**Request body:**
```json
{
  "user": "pedram",
  "destination": "Montreal"
}
```

**Response (201):**
```json
{
  "id": "booking-uuid",
  "user": "pedram",
  "destination": "Montreal",
  "status": "confirmed"
}
```

---

### GET `/bookings/<booking_id>`
Retrieves details of a specific booking.

**Example response:**
```json
{
  "id": "booking-uuid",
  "user": "pedram",
  "destination": "Montraeal",
  "status": "confirmed"
}
```

---

### PATCH `/bookings/<booking_id>`
Updates the status of an existing booking.

**Request body:**
```json
{
  "status": "cancelled"
}
```

**Example response:**
```json
{
  "id": "booking-uuid",
  "user": "pedram",
  "destination": "Montreal",
  "status": "cancelled"
}
```

---

## Notification Service (`5002`)

### POST `/notify/email`
Simulates sending an email notification when a booking is created.

**Request body:**
```json
{
  "user": "pedram",
  "message": "Your booking to Toronto is confirmed!You are going!"
}
```

**Response:**
```json
{
  "status": "email sent",
  "user": "pedram"
}
```

