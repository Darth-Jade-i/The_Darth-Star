#!/usr/bin/python3


import mysql.connector
from mysql.connector import Error


def create_connection():
    """Establish a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='knight',  # Replace with your MySQL username
            password='#6EdeniaKnight9#',
            #Replace line 13 with your password or leave blank
            #if using auth_socket
            database='the_darth_star'
        )
        if connection.is_connected():
            print("Connection to MySQL database established successfully.")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None


def close_connection(connection):
    """Close the connection to the MySQL database."""
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
