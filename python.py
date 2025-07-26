from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/jenkinsdata', methods=['POST'])
def receive_data():
    data = request.json
    conn = mysql.connector.connect(user='youruser', password='yourpass', host='localhost', database='jenkins_pipeline_db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO jenkins_builds (user, job_name, build_number, version, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """, (data['user'], data['job_name'], data['build_number'], data['version'], data['timestamp']))
    conn.commit()
    return 'OK', 200