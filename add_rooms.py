from app import app, db, Room

# Define sample rooms with amenities and images
sample_rooms = [
    {
        "room_number": "101",
        "room_type": "Single",
        "price": 1200.0,
        "amenities": "WiFi, TV, Air Conditioning",
        "image": "single-room.jpg"
    },
    {
        "room_number": "102",
        "room_type": "Double",
        "price": 1800.0,
        "amenities": "WiFi, TV, Air Conditioning, Mini Bar",
        "image": "double-room.jpg"
    },
    {
        "room_number": "103",
        "room_type": "Deluxe",
        "price": 2500.0,
        "amenities": "WiFi, TV, Air Conditioning, Mini Bar, Balcony",
        "image": "deluxe-room.jpg"
    },
    {
        "room_number": "104",
        "room_type": "Suite",
        "price": 3000.0,
        "amenities": "WiFi, TV, Air Conditioning, Mini Bar, Balcony, Kitchenette",
        "image": "suite-room.jpg"
    },
    {
        "room_number": "105",
        "room_type": "Single",
        "price": 1100.0,
        "amenities": "WiFi, TV",
        "image": "single-room.jpg"
    },
    {
        "room_number": "106",
        "room_type": "Double",
        "price": 1700.0,
        "amenities": "WiFi, TV, Air Conditioning",
        "image": "double-room.jpg"
    },
    {
        "room_number": "107",
        "room_type": "Deluxe",
        "price": 2600.0,
        "amenities": "WiFi, TV, Air Conditioning, Mini Bar",
        "image": "deluxe-room.jpg"
    },
    {
        "room_number": "108",
        "room_type": "Suite",
        "price": 3200.0,
        "amenities": "WiFi, TV, Air Conditioning, Mini Bar, Balcony, Kitchenette",
        "image": "suite-room.jpg"
    },
]

with app.app_context():
    for room_data in sample_rooms:
        existing = Room.query.filter_by(room_number=room_data["room_number"]).first()
        if not existing:
            new_room = Room(
                room_number=room_data["room_number"],
                room_type=room_data["room_type"],
                price=room_data["price"],
                capacity=room_data.get("capacity", 2),
                amenities=room_data.get("amenities", ""),
                image=room_data.get("image", "default-room.jpg")
            )
            # Uncomment if Room model has this attribute
            # new_room.is_available = True
            db.session.add(new_room)
        else:
            # Update existing room with image if it doesn't have one
            if not existing.image:
                existing.image = room_data.get("image", "default-room.jpg")

    db.session.commit()
    print("Rooms added/updated successfully with images.")







