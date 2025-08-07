# 🏨 Enhanced Hotel Booking System

A comprehensive hotel booking management system built with Flask, featuring advanced room categorization, payment processing, and professional UI design.

## 🆕 Latest Enhancements

### ✨ New Features Added:
- **A/C and Non-A/C Room Separation**: Rooms are now categorized with distinct pricing and visual indicators
- **Professional Hotel UI**: Modern, hotel-industry-inspired background and styling
- **Admin Contact Information**: Centralized contact management with phone and email display
- **Excel Export**: Download complete booking data in Excel format for admin analysis
- **QR Code Payments**: Generate UPI QR codes for seamless payment processing
- **Enhanced Admin Dashboard**: Improved booking management with detailed financial tracking

## 🏨 Features

### For Guests:
- **User Registration & Login**: Secure authentication with profile management
- **Room Categorization**: Filter rooms by A/C and Non-A/C with visual badges
- **Advanced Room Browsing**: Professional room cards with amenity details
- **Smart Booking System**: Date-based availability checking with conflict resolution
- **QR Code Payments**: Scan-to-pay functionality with UPI integration
- **Booking Management**: View, modify, and cancel reservations
- **Professional UI**: Hotel-themed design with elegant styling

### For Hotel Administrators:
- **Enhanced Admin Dashboard**: Complete overview with contact information display
- **Room Management**: Add A/C/Non-A/C rooms with detailed specifications
- **Excel Booking Export**: Download comprehensive booking data for analysis
- **Revenue Tracking**: Real-time financial monitoring with detailed calculations
- **Contact Management**: Centralized hotel contact information
- **Professional Tables**: Modern Bootstrap-styled data presentation

## 🛠 Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login with secure password hashing
- **Data Export**: Pandas + OpenPyXL for Excel generation
- **QR Codes**: qrcode library with UPI payment integration
- **Frontend**: HTML, CSS, Bootstrap 5 with custom hotel styling
- **Images**: Pillow for QR code image processing

## 📦 Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd hotel-booking-system
```

2. **Create a virtual environment:**
```bash
python -m venv hotel_booking_env
source hotel_booking_env/bin/activate  # On Windows: hotel_booking_env\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Initialize the enhanced database:**
```bash
python migrate_enhanced_db.py
```

5. **Add sample A/C and Non-A/C rooms:**
```bash
python add_sample_rooms.py
```

6. **Run the application:**
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🗄 Enhanced Database Schema

### Rooms (Enhanced)
- Room categorization (A/C/Non-A/C) with `has_ac` boolean field
- Pricing differentiation based on A/C status
- Advanced amenity management
- Professional image handling

### Admin Configuration (New)
- Hotel contact information (phone, email, address)
- UPI payment details for QR code generation
- Centralized admin settings management

### Bookings (Enhanced)
- Improved total amount calculations
- Better payment status tracking
- Excel export compatibility

## 🎯 Usage Guide

### For Hotel Guests:
1. **Register/Login**: Create account or sign in
2. **Filter Rooms**: Use A/C/Non-A/C filters to find preferred accommodation
3. **Book Rooms**: Select dates and confirm booking
4. **Pay with QR**: Scan QR code for instant UPI payments
5. **Manage Bookings**: View and modify reservations

### For Hotel Administrators:
1. **Access Admin Dashboard**: Login with admin credentials
2. **Manage Rooms**: Add A/C and Non-A/C rooms with appropriate pricing
3. **Export Data**: Download booking data in Excel format
4. **Monitor Revenue**: Track earnings with detailed financial reports
5. **Update Contact Info**: Manage hotel contact information

## 🎨 UI/UX Enhancements

### Professional Hotel Theme:
- **Elegant Background**: Multi-layered gradient with subtle hotel patterns
- **Modern Cards**: Professional room display with hover effects
- **Visual Indicators**: Color-coded A/C/Non-A/C badges
- **Responsive Design**: Mobile-friendly layout with Bootstrap 5
- **Professional Typography**: Hotel-industry appropriate fonts

### Enhanced User Experience:
- **Filter System**: Easy A/C/Non-A/C room filtering
- **QR Payment**: Modern payment solution with visual instructions
- **Contact Display**: Prominent admin contact information
- **Excel Export**: One-click booking data download
- **Professional Tables**: Clean, organized data presentation

## 💳 Payment System

### QR Code Integration:
- **UPI Compatibility**: Works with PhonePe, Google Pay, Paytm, etc.
- **Automatic Generation**: QR codes created for each booking
- **Amount Integration**: Pre-filled payment amounts
- **Admin Contact**: Payment support information displayed

## 📊 Admin Features

### Enhanced Dashboard:
- **Contact Information**: Hotel details prominently displayed
- **Excel Export**: Download complete booking data
- **Revenue Tracking**: Real-time financial monitoring
- **Room Management**: A/C/Non-A/C categorization
- **Professional Design**: Modern admin interface

### Excel Export Features:
- **Comprehensive Data**: All booking details in one file
- **Customer Information**: Complete guest details
- **Financial Analysis**: Revenue calculations and payment status
- **A/C Classification**: Room type categorization
- **Date Management**: Check-in/out tracking

## 🔧 Development

### Project Structure:
```
hotel-booking-system/
├── app.py                          # Enhanced Flask application
├── migrate_enhanced_db.py          # Database migration script
├── add_sample_rooms.py            # Sample A/C/Non-A/C rooms
├── requirements.txt               # Updated dependencies
├── templates/
│   ├── admin_dashboard.html       # Enhanced admin interface
│   ├── rooms.html                 # Room filtering and display
│   ├── pay.html                   # QR code payment page
│   └── ...                        # Other templates
├── static/
│   └── style.css                  # Professional hotel styling
└── README.md                      # This documentation
```

### Database Migrations:
- **Enhanced Migration**: Run `migrate_enhanced_db.py` for new features
- **Sample Data**: Use `add_sample_rooms.py` for demonstration
- **Backward Compatibility**: Existing data preserved during upgrades

## 🚀 Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Migrate database with new features
python migrate_enhanced_db.py

# Add sample A/C and Non-A/C rooms
python add_sample_rooms.py

# Run the enhanced application
python app.py
```

## 📋 Feature Checklist

- ✅ **A/C and Non-A/C Room Separation**: Complete categorization system
- ✅ **Professional Hotel UI**: Modern background and styling
- ✅ **Admin Contact Information**: Centralized contact management
- ✅ **Excel Booking Export**: Comprehensive data download
- ✅ **QR Code Payment System**: UPI integration with visual QR codes
- ✅ **Enhanced Admin Dashboard**: Improved management interface
- ✅ **Mobile Responsive Design**: Works on all devices
- ✅ **Professional Typography**: Hotel-appropriate fonts and styling

## 🔐 Security Features

- **Enhanced Password Security**: Werkzeug hashing with salt
- **SQL Injection Prevention**: SQLAlchemy ORM protection
- **CSRF Protection**: Form validation and security
- **Session Management**: Secure user authentication
- **Data Validation**: Input sanitization and validation

## 📞 Support & Contact

- **Admin Contact**: Displayed in payment and admin sections
- **Technical Support**: Contact hotel administration
- **Documentation**: Comprehensive README and code comments

## 🎯 Demo Credentials

While registering, choose whether you are a **User** or **Admin**:
- **Admins**: Access to dashboard with room management and booking export
- **Users**: Room browsing, booking, and payment functionality

## 🤝 Contribution

Feel free to fork this repo and suggest improvements via pull requests!

## 📄 License

This project is licensed under the MIT License.

---

**Professional Hotel Booking System - Enhanced with A/C categorization, QR payments, and modern UI design** 🏨✨
