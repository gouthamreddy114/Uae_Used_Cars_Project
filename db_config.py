import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nanireddy@114",
        database="uae_used_cars_db"
    )
    return conn
