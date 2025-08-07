#!/usr/bin/env python3
"""
Sample Room Creation Script
Adds sample A/C and Non-A/C rooms to demonstrate the enhanced hotel booking system
"""

from app import app, db, Room

def add_sample_rooms():
    with app.app_context():
        print("Adding sample rooms...")
        
        # Sample A/C Rooms
        ac_rooms = [
            {
                'room_number': 'AC101',
                'room_type': 'Deluxe',
                'price': 2500.0,
                'capacity': 2,
                'amenities': 'Air Conditioning, Wi-Fi, TV, Mini Bar, Room Service',
                'has_ac': True
            },
            {
                'room_number': 'AC102',
                'room_type': 'Suite',
                'price': 4000.0,
                'capacity': 4,
                'amenities': 'Air Conditioning, Wi-Fi, TV, Mini Bar, Room Service, Balcony, Jacuzzi',
                'has_ac': True
            },
            {
                'room_number': 'AC103',
                'room_type': 'Standard',
                'price': 1800.0,
                'capacity': 2,
                'amenities': 'Air Conditioning, Wi-Fi, TV, Room Service',
                'has_ac': True
            },
            {
                'room_number': 'AC201',
                'room_type': 'Deluxe',
                'price': 2700.0,
                'capacity': 3,
                'amenities': 'Air Conditioning, Wi-Fi, TV, Mini Bar, Room Service, Sea View',
                'has_ac': True
            }
        ]
        
        # Sample Non-A/C Rooms
        non_ac_rooms = [
            {
                'room_number': 'NAC101',
                'room_type': 'Standard',
                'price': 1200.0,
                'capacity': 2,
                'amenities': 'Fan, Wi-Fi, TV, Room Service',
                'has_ac': False
            },
            {
                'room_number': 'NAC102',
                'room_type': 'Deluxe',
                'price': 1600.0,
                'capacity': 2,
                'amenities': 'Fan, Wi-Fi, TV, Room Service, Balcony',
                'has_ac': False
            },
            {
                'room_number': 'NAC103',
                'room_type': 'Standard',
                'price': 1000.0,
                'capacity': 2,
                'amenities': 'Fan, Wi-Fi, TV',
                'has_ac': False
            },
            {
                'room_number': 'NAC201',
                'room_type': 'Deluxe',
                'price': 1800.0,
                'capacity': 3,
                'amenities': 'Fan, Wi-Fi, TV, Room Service, Garden View',
                'has_ac': False
            }
        ]
        
        all_rooms = ac_rooms + non_ac_rooms
        rooms_added = 0
        
        for room_data in all_rooms:
            # Check if room already exists
            existing_room = Room.query.filter_by(room_number=room_data['room_number']).first()
            if not existing_room:
                room = Room(**room_data)
                db.session.add(room)
                rooms_added += 1
                print(f"✓ Added {room_data['room_number']} ({'A/C' if room_data['has_ac'] else 'Non-A/C'}) - ₹{room_data['price']}")
            else:
                print(f"• Room {room_data['room_number']} already exists, skipping...")
        
        if rooms_added > 0:
            db.session.commit()
            print(f"\n🎉 Successfully added {rooms_added} sample rooms!")
        else:
            print("\n📝 No new rooms added (all rooms already exist)")
        
        # Display summary
        total_rooms = Room.query.count()
        ac_count = Room.query.filter_by(has_ac=True).count()
        non_ac_count = Room.query.filter_by(has_ac=False).count()
        
        print(f"\n📊 Current Room Statistics:")
        print(f"Total Rooms: {total_rooms}")
        print(f"A/C Rooms: {ac_count}")
        print(f"Non-A/C Rooms: {non_ac_count}")

if __name__ == "__main__":
    try:
        add_sample_rooms()
    except Exception as e:
        print(f"❌ Error adding sample rooms: {e}")
        import traceback
        traceback.print_exc()