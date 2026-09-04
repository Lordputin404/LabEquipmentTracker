import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def get_equipment_stats():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM equipment")
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM equipment
        WHERE condition_status = 'Working'
    """)
    working = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM equipment
        WHERE condition_status = 'Maintenance'
    """)
    maintenance = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM equipment
        WHERE condition_status = 'Damaged'
    """)
    damaged = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return total, working, maintenance, damaged

def get_recent_equipment():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT equipment_name, lab_name, condition_status
        FROM equipment
        ORDER BY id DESC
        LIMIT 5
    """)

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records