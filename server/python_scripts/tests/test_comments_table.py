import sys
import os

# Add the directory containing db_handler.py to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from mysql.connector import Error
# Import the function to create a connection
from db_handler import create_connection, close_connection

def test_comments_table_exists():
    try:
        # Create a connection to the database
        conn = create_connection()
        cursor = conn.cursor()
        # Use the `the_darth_star` database
        cursor.execute("USE the_darth_star;")
        # Check if the `comments` table exists
        cursor.execute("SHOW TABLES LIKE 'comments';")
        result = cursor.fetchone()
        assert result is not None, "Test Failed: 'comments' table doesn't exist"
        print("Test Passed: 'comments' table exists")
    except Error as e:
        print(f"Test Failed: {e}")
    finally:
        close_connection(conn)

def test_comments_table_structure():
    try:
        # Create a connection to the database
        conn = create_connection()
        cursor = conn.cursor()
        # Use the `the_darth_star` database
        cursor.execute("USE the_darth_star;")
        # Describe the structure of the `comments` table
        cursor.execute("DESCRIBE comments;")
        result = cursor.fetchall()
        # Updated expected table structure
        expected_structure = [
            ('id', 'int', 'NO', 'PRI', None, 'auto_increment'),
            ('blog_id', 'int', 'YES', 'MUL', None, ''),
            ('user_id', 'int', 'YES', 'MUL', None, ''),
            ('content', 'text', 'NO', '', None, ''),
            ('created_at', 'timestamp', 'YES', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED')
        ]
        # Check if the fetched structure matches the expected structure
        for i, column in enumerate(result):
            assert column[:6] == expected_structure[i], (
                f"Test Failed: Column {column[0]} does not match "
                "the expected structure."
            )
            print("Test Passed: 'comments' table structure is correct.")
    except Error as e:
        print(f"Test Failed: {e}")
    finally:
        close_connection(conn)

if __name__ == "__main__":
    test_comments_table_exists()
    test_comments_table_structure()
