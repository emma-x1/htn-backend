import json
import sqlite3
from datetime import datetime

with open('example_data.json') as file:
    data = json.load(file)

conn = sqlite3.connect('htn_backend.db')
cursor = conn.cursor()

for hacker in data:
    badge_code = hacker['badge_code']
    name = hacker['name']
    email = hacker['email']
    phone = hacker['phone']
    updated_at = datetime.now().isoformat()

    cursor.execute('''
    INSERT OR IGNORE INTO hackers (badge_code, name, email, phone)
    VALUES (?, ?, ?, ?)
    ''', (badge_code, name, email, phone))

    """
    for scan in hacker['scans']:
        activity_name = scan['activity_name']
        activity_category = scan['activity_category']
        scanned_at = scan['scanned_at']

        cursor.execute('''
            INSERT OR IGNORE INTO scans (badge_code, activity_name, activity_category, scanned_at)
            VALUES (?, ?, ?, ?)
            ''', (badge_code, activity_name, activity_category, scanned_at))
    """

conn.commit()
conn.close()