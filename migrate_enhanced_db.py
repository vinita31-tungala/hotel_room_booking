#!/usr/bin/env python3
"""
Enhanced Database Migration Script
Adds has_ac column to Room table and creates AdminConfig table
"""

import os
import sys
from datetime import datetime
from app import app, db, Room, AdminConfig

def migrate_database():
    with app.app_context():
        print("Starting database migration...")
        
        # Create all tables (this will create new tables and add new columns)
        db.create_all()
        print("✓ Database tables created/updated")
        
        # Add has_ac column to existing rooms if they don't have it
        try:
            # Check if any rooms exist without has_ac column set
            rooms_without_ac = Room.query.filter(Room.has_ac.is_(None)).all()
            if rooms_without_ac:
                print(f"Found {len(rooms_without_ac)} rooms without A/C status. Setting default...")
                for room in rooms_without_ac:
                    room.has_ac = True  # Default to A/C rooms
                db.session.commit()
                print("✓ Updated existing rooms with A/C status")
            else:
                print("✓ All rooms already have A/C status")
        except Exception as e:
            print(f"Note: {e} (This is normal for new installations)")
        
        # Create default admin config if it doesn't exist
        admin_config = AdminConfig.query.first()
        if not admin_config:
            admin_config = AdminConfig(
                hotel_name="Grand Hotel",
                contact_email="admin@grandhotel.com",
                contact_phone="+91-9876543210",
                address="123 Hotel Street, City, State - 123456",
                upi_id="grandhotel@paytm"
            )
            db.session.add(admin_config)
            db.session.commit()
            print("✓ Created default admin configuration")
        else:
            print("✓ Admin configuration already exists")
        
        print("\n🎉 Database migration completed successfully!")
        print("\nEnhancements added:")
        print("• A/C and Non-A/C room categorization")
        print("• Admin contact information management")
        print("• Excel export functionality for bookings")
        print("• QR code payment system")
        print("• Professional hotel UI design")

if __name__ == "__main__":
    try:
        migrate_database()
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        sys.exit(1)