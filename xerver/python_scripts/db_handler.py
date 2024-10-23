import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='knight',
            password='#6EdeniaKnight9#',  # Replace with actual password
            database='the_darth_star'
        )
        if conn.is_connected():
            print("Connection to MySQL database established successfully.")
        return conn
    except Error as e:
        print(f"Error: '{e}'")
        return None

def close_connection(conn, cursor=None):
    """Close the connection to the database and cursor if provided."""
    if cursor is not None:
        cursor.close()
    if conn is not None and conn.is_connected():
        conn.close()
        print("Connection to MySQL database closed successfully.")
