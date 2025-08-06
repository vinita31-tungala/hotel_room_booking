# Room Images Directory

This directory is designed to store room images for the hotel booking system.

## Current Implementation

The application currently uses CSS-generated background images for room types:
- Single rooms: Coral gradient with bed icon
- Double rooms: Teal gradient with twin bed icons  
- Deluxe rooms: Purple gradient with luxury indicators
- Suite rooms: Warm gradient with premium amenities

## Adding Real Images

To replace the CSS placeholders with real room photos:

1. Add high-quality room images (recommended: 800x600 pixels) to this directory
2. Name them according to room types:
   - `single-room.jpg` - for Single rooms
   - `double-room.jpg` - for Double rooms  
   - `deluxe-room.jpg` - for Deluxe rooms
   - `suite-room.jpg` - for Suite rooms

3. Update the `rooms.html` template to use actual images instead of CSS classes:
   ```html
   <img src="{{ url_for('static', filename='images/rooms/' + room.image) }}" 
        alt="{{ room.room_type }} Room" class="room-image">
   ```

4. Adjust the CSS accordingly to style the `<img>` elements instead of background images.

## Image Requirements
- Format: JPG, PNG, or WebP
- Size: 800x600 pixels (4:3 aspect ratio)
- File size: Under 500KB for optimal loading
- Quality: High resolution, well-lit room photos