#!/usr/bin/env python3
"""
Database migration script to add phone, address, and state fields to existing User table
"""
import sqlite3
import os

def migrate_database():
    db_path = os.path.join('instance', 'hotel.db')
    
    if not os.path.exists(db_path):
        print("Database not found. It will be created when the app runs.")
        return
    
    print(f"Migrating database at {db_path}")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if the new columns already exist
        cursor.execute("PRAGMA table_info(user)")
        columns = [column[1] for column in cursor.fetchall()]
        
        migrations_needed = []
        if 'phone' not in columns:
            migrations_needed.append("ALTER TABLE user ADD COLUMN phone VARCHAR(15)")
        if 'address' not in columns:
            migrations_needed.append("ALTER TABLE user ADD COLUMN address TEXT")
        if 'state' not in columns:
            migrations_needed.append("ALTER TABLE user ADD COLUMN state VARCHAR(50)")
        
        if not migrations_needed:
            print("Database is already up to date.")
            return
        
        # Execute migrations
        for migration in migrations_needed:
            print(f"Executing: {migration}")
            cursor.execute(migration)
        
        conn.commit()
        print("Migration completed successfully!")
        
    except Exception as e:
        print(f"Migration failed: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    migrate_database()