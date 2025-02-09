from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect('htn_backend.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/users', methods=['GET'])
def all_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM hackers')
    users = cursor.fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])

@app.route('/users/<badge_code>', methods=['GET'])
def user_by_badge_code(badge_code,):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM hackers WHERE badge_code = ?', (badge_code))
    user = cursor.fetchone()
    conn.close()
    return jsonify(dict(user))

@app.route('/update/<badge_code>', methods=['POST'])
def update_user(badge_code):
    data = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    if 'name' in data:
        cursor.execute('''
        UPDATE hackers
        SET name = ?
        WHERE badge_code = ?
        ''', (data['name'], badge_code))
    if 'email' in data:
        cursor.execute('''
        UPDATE hackers
        SET email = ?
        WHERE badge_code = ?
        ''', (data['email'], badge_code))
    if 'phone' in data:
        cursor.execute('''
        UPDATE hackers
        SET phone = ?
        WHERE badge_code = ?
        ''', (data['phone'], badge_code))
    conn.commit()
    conn.close()
    return 'User updated'

@app.route('/scan', methods=['POST'])
def scan_user():
    data = request.get_json()
    badge_code = data.get('badge_code')
    activity_name = data.get('activity_name')
    activity_category = data.get('activity_category')
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO scans (badge_code, activity_name, activity_category, scanned_at)
    VALUES (?, ?, ?, datetime('now'))
    ''', (badge_code, activity_name, activity_category))
    conn.commit()
    conn.close()
    return 'Scan recorded'

@app.route('/scan_data', methods=['GET'])
def scan_data():
    min_frequency = request.args.get('min_frequency', type=int)
    max_frequency = request.args.get('max_frequency', type=int)
    activity_category = request.args.get('activity_category')
    conn = connect_db()
    cursor = conn.cursor()

    query = '''
    SELECT activity_name, activity_category, COUNT(*) as frequency
    FROM scans
    '''
    
    if activity_category:
        query += ' WHERE activity_category = ?'
        params = [activity_category]
    
    query += ' GROUP BY activity_name'

    if min_frequency:
        query += ' HAVING frequency >= ?'
        params.append(min_frequency)
    if max_frequency:
        query += ' AND frequency <= ?'
        params.append(max_frequency)

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return jsonify([dict(row) for row in results])

        