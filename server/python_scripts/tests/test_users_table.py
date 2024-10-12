from db_handler import create_connection, close_connection
import sys
import os
import mysql.connector
from mysql.connector import Error

# Add the directory containing db_handler.py to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_users_table_exists():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("USE the_darth_star;")
        cursor.execute("SHOW TABLES LIKE 'users';")
        result = cursor.fetchone()
        assert result is not None, "Test Failed: 'users' table doesn't exist"
        print("Test Passed: 'users' table exists")
    except Error as e:
        print(f"Test Failed: {e}")
    finally:
        close_connection(conn)


def test_users_table_structure():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("USE the_darth_star;")
        cursor.execute("DESCRIBE users;")
        result = cursor.fetchall()
        expected_structure = [
            ('id', 'int', 'NO', 'PRI', None, 'auto_increment'),
            ('username', 'varchar(100)', 'NO', '', None, ''),
            ('password_hash', 'varchar(255)', 'NO', '', None, ''),
            ('email', 'varchar(100)', 'NO', 'UNI', None, ''),
            ('created_at', 'timestamp', 'YES', '', 'CURRENT_TIMESTAMP',
             'DEFAULT_GENERATED')
        ]

        for i, column in enumerate(result):
            assert column[:6] == expected_structure[i], (
                f"Test Failed: Column {
                    column[0]} does not match expected structure."
            )
            print("Test Passed: 'users' table structure is correct.")
    except Error as e:
        print(f"Test Failed: {e}")
    finally:
        close_connection(conn)


if __name__ == "__main__":
    test_users_table_exists()
    test_users_table_structure()
