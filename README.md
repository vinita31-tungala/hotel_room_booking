🏨 Hotel Room Booking System

This is a Flask-based web application for booking hotel rooms. The system allows both **Users** and **Admins** to register and log in. Admins can manage rooms and view all bookings, while users can view available rooms and make bookings.

 🚀 Features

 ✅ General
- User and Admin registration/login
- Role selection on registration page
- Password hashing for security
- SQLite database with SQLAlchemy ORM
- Bootstrap-based frontend

👤 User Features
- Register and log in as a user
- View available rooms
- Book a room
- View booking history
- Cancel bookings
- View booking status

🛠️ Admin Features
- Register and log in as admin
- Dashboard to view all bookings
- Add and manage hotel rooms
- View cancelled bookings
- Manage room availability
- View detailed booking info

 🏨 Room Features
- Room number, type, price
- Amenities and capacity
- Room availability status

 🧱 Tech Stack

| Category     | Technologies Used                     |
|--------------|----------------------------------------|
| Backend      | Python, Flask, SQLAlchemy              |
| Frontend     | HTML, CSS, Bootstrap, Jinja2           |
| Database     | SQLite                                 |
| Authentication | Flask-Login, Werkzeug Security       |


 📁 Project Structure

hotel_room_booking/
│
├── app.py # Main Flask application
├── models.py # SQLAlchemy models
├── templates/ # HTML templates
│ ├── login.html
│ ├── register.html
│ ├── rooms.html
│ ├── my_bookings.html
│ ├── admin_dashboard.html
│ └── ...
├── static/ # CSS, JS, images
├── add_rooms.py # Script to populate rooms in DB
├── requirements.txt
└── README.md

 🛠️ Installation & Setup

1. Clone the repository

bash
git clone https://github.com/yourusername/hotel-room-booking.git
cd hotel-room-booking

Create and activate virtual environment
'''bash
python -m venv venv
venv\Scripts\activate

 Initialize the database
'''bash
from app import db
db.create_all()

Or you can run this inside a Python shell:
'''Powershell
from app import db
db.create_all()

 Populate rooms (optional but recommended)
'''bash
python add_rooms.py

Run the application
'''bash
python app.py

Go to http://127.0.0.1:5000 in your browser.

🔐 Credentials for Demo
While registering, choose whether you are a User or Admin

Admins are redirected to a dashboard with extra controls.

🤝 Contribution
Feel free to fork this repo and suggest improvements via pull requests!
