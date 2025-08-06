import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

basedir = os.path.abspath(os.path.dirname(__file__))
db_folder = os.path.join(basedir, 'instance')
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(db_folder, 'hotel.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# ==================== Models ====================

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Length for hash
    phone = db.Column(db.String(15), nullable=True)
    address = db.Column(db.Text, nullable=True)
    state = db.Column(db.String(50), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(20), unique=True, nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    capacity = db.Column(db.Integer, default=2)
    amenities = db.Column(db.String(200))
    image = db.Column(db.String(100), default='default-room.jpg')

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    check_in = db.Column(db.Date)  # Changed to Date type
    check_out = db.Column(db.Date)
    is_cancelled = db.Column(db.Boolean, default=False)
    payment_status = db.Column(db.String(20), default='pending')

    user = db.relationship('User', backref='bookings')
    room = db.relationship('Room', backref='bookings')

# ==================== User Loader ====================

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ==================== Routes ====================

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    else:
        return redirect(url_for('user_dashboard'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        phone = request.form.get('phone', '')
        address = request.form.get('address', '')
        state = request.form.get('state', '')
        role = request.form.get('role')

        # Validation
        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('register'))

        if len(password) < 6:
            flash('Password must be at least 6 characters long')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))

        if phone and User.query.filter_by(phone=phone).first():
            flash('Phone number already registered')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)  # Default method is 'pbkdf2:sha256'

        is_admin = True if role == 'admin' else False
        new_user = User(
            username=username, 
            email=email, 
            password=hashed_password, 
            phone=phone if phone else None,
            address=address if address else None,
            state=state if state else None,
            is_admin=is_admin
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        flash('Registration successful! Welcome to our hotel booking system.')
        if is_admin:
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('user_dashboard'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')

    return render_template('login.html')

@app.route('/admin_dashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash("Access denied.")
        return redirect(url_for('home'))

    rooms = Room.query.all()
    bookings = Booking.query.all()
    total_revenue = sum([b.room.price for b in bookings if b.payment_status == 'paid'])

    if request.method == 'POST':
        room_number = request.form['room_number']
        room_type = request.form['room_type']
        price = float(request.form['price'])
        capacity = int(request.form['capacity'])
        amenities = request.form['amenities']

        room = Room(room_number=room_number, room_type=room_type, price=price,
                    capacity=capacity, amenities=amenities)
        db.session.add(room)
        db.session.commit()
        flash('Room added successfully!')

    return render_template('admin_dashboard.html', rooms=rooms, bookings=bookings, revenue=total_revenue)

@app.route('/user_dashboard')
@login_required
def user_dashboard():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('user_dashboard.html', bookings=bookings)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/rooms')
@login_required
def view_rooms():
    room_type = request.args.get('type')
    min_price = request.args.get('min_price', 0, type=float)
    max_price = request.args.get('max_price', 10000, type=float)
    capacity = request.args.get('capacity', type=int)
    check_in_str = request.args.get('check_in')
    check_out_str = request.args.get('check_out')

    query = Room.query

    if room_type:
        query = query.filter_by(room_type=room_type)
    if capacity:
        query = query.filter(Room.capacity >= capacity)
    query = query.filter(Room.price >= min_price, Room.price <= max_price)

    rooms = query.all()

    if check_in_str and check_out_str:
        try:
            check_in = datetime.strptime(check_in_str, '%Y-%m-%d').date()
            check_out = datetime.strptime(check_out_str, '%Y-%m-%d').date()
            if check_out <= check_in:
                flash('Check-out date must be after check-in date.')
                return redirect(url_for('view_rooms'))
        except ValueError:
            flash('Invalid date format for check-in or check-out. Use YYYY-MM-DD.')
            return redirect(url_for('view_rooms'))

        available_rooms = []
        for room in rooms:
            conflict = Booking.query.filter(
                Booking.room_id == room.id,
                Booking.is_cancelled == False,
                Booking.check_in <= check_out,
                Booking.check_out >= check_in
            ).first()
            if not conflict:
                available_rooms.append(room)
        rooms = available_rooms

    return render_template('rooms.html', rooms=rooms, check_in=check_in_str, check_out=check_out_str)

@app.route('/book/<int:room_id>', methods=['GET', 'POST'])
@login_required
def book_room(room_id):
    room = Room.query.get_or_404(room_id)
    if request.method == 'POST':
        check_in = request.form['check_in']
        check_out = request.form['check_out']
        try:
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()
            if check_out_date <= check_in_date:
                flash('Check-out date must be after check-in date.')
                return redirect(url_for('book_room', room_id=room_id))
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.')
            return redirect(url_for('book_room', room_id=room_id))

        conflict = Booking.query.filter(
            Booking.room_id == room.id,
            Booking.is_cancelled == False,
            Booking.check_in <= check_out_date,
            Booking.check_out >= check_in_date
        ).first()
        if conflict:
            flash('Room is not available for the selected dates.')
            return redirect(url_for('view_rooms'))

        booking = Booking(user_id=current_user.id, room_id=room.id,
                          check_in=check_in_date, check_out=check_out_date)
        db.session.add(booking)
        db.session.commit()
        flash('Room booked successfully!')
        return redirect(url_for('my_bookings'))

    return render_template('book.html', room=room)

@app.route('/delete_room/<int:room_id>')
@login_required
def delete_room(room_id):
    if not current_user.is_admin:
        return redirect(url_for('home'))
    Room.query.filter_by(id=room_id).delete()
    db.session.commit()
    flash('Room deleted.')
    return redirect(url_for('admin_dashboard'))

@app.route('/my_bookings')
@login_required
def my_bookings():
    bookings = Booking.query.filter_by(user_id=current_user.id, is_cancelled=False).all()
    return render_template('my_bookings.html', bookings=bookings)

@app.route('/delete_booking/<int:booking_id>', methods=['POST'])
@login_required
def delete_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.user_id != current_user.id:
        flash('Unauthorized action.')
        return redirect(url_for('my_bookings'))
    booking.is_cancelled = True
    db.session.commit()
    flash('Booking cancelled successfully.')
    return redirect(url_for('my_bookings'))

@app.route('/cancelled_bookings')
@login_required
def cancelled_bookings():
    cancelled = Booking.query.filter_by(user_id=current_user.id, is_cancelled=True).all()
    return render_template('cancelled_bookings.html', bookings=cancelled)

@app.route('/pay/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def pay(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.user_id != current_user.id:
        flash('Unauthorized payment attempt.')
        return redirect(url_for('my_bookings'))
    if booking.is_cancelled:
        flash('Cannot pay for a cancelled booking.')
        return redirect(url_for('my_bookings'))
    if request.method == 'POST':
        booking.payment_status = 'paid'
        db.session.commit()
        flash('Payment successful! Thank you.')
        return redirect(url_for('my_bookings'))
    return render_template('pay.html', booking=booking)

@app.route('/update_profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    if request.method == 'POST':
        current_user.username = request.form['username']
        current_user.email = request.form['email']
        db.session.commit()
        flash('Profile updated successfully.')
        return redirect(url_for('user_dashboard'))
    return render_template('update_profile.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

