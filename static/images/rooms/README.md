# Room Images Directory

This directory contains high-quality room images for the hotel booking system.

## Current Implementation

The application now uses real room photographs downloaded from Unsplash:
- `single-room.jpg` - Elegant single room with modern furnishing
- `double-room.jpg` - Spacious double room with twin beds
- `deluxe-room.jpg` - Luxury deluxe room with premium amenities
- `suite-room.jpg` - Premium suite with sophisticated design

## Image Details

All images are:
- **Format**: JPG
- **Resolution**: 800x600 pixels (optimized for web)
- **Quality**: High-resolution professional photography
- **Source**: Unsplash (royalty-free)
- **Size**: Optimized for fast loading (60-100KB each)

## Replacing Images

To replace any room image:

1. Replace the corresponding file in this directory
2. Maintain the same filename format:
   - `single-room.jpg` - for Single rooms
   - `double-room.jpg` - for Double rooms  
   - `deluxe-room.jpg` - for Deluxe rooms
   - `suite-room.jpg` - for Suite rooms

3. **Recommended specifications**:
   - Format: JPG, PNG, or WebP
   - Size: 800x600 pixels (4:3 aspect ratio)
   - File size: Under 500KB for optimal loading
   - Quality: High resolution, well-lit room photos

## Technical Implementation

The images are displayed using the `<img>` tag with:
- `object-fit: cover` for proper aspect ratio
- Hover zoom effects for interactivity
- Responsive design for all screen sizes
- Lazy loading for performance optimization