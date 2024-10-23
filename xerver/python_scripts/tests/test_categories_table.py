import sys
import os
from mysql.connector import Error
import mysql.connector

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from db_handler import create_connection, close_connection
from config import db_config
from test_cleanup import cleanup_test_data


def test_categories_table_exists():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Check if the categories table exists
        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_schema = DATABASE()
            AND table_name = 'categories'
        """)

        result = cursor.fetchone()

        assert result[0] == 1, "Test Failed: 'categories' table doesn't exist"
        print("Test Passed: 'categories' table exists")

        # Check the structure of the table
        cursor.execute("DESCRIBE categories")
        columns = cursor.fetchall()

        expected_columns = [
            ('id', 'int', 'NO', 'PRI', None, 'auto_increment'),
            ('name', 'varchar(100)', 'NO', '', None, ''),
            ('description', 'text', 'YES', '', None, '')
        ]

        assert len(columns) == len(expected_columns), f"Test Failed: 'categories' table has incorrect number of columns. Expected {len(expected_columns)}, got {len(columns)}"

        for actual, expected in zip(columns, expected_columns):
            assert actual[:6] == expected, f"Test Failed: Column {actual[0]} does not match expected structure. Expected {expected}, got {actual[:6]}"

        print("Test Passed: 'categories' table has the correct structure")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        assert False, "Test Failed: Unable to connect to the database or execute query"
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


def test_categories_table_structure():
    try:
        # Create a connection to the database
        conn = create_connection()
        cursor = conn.cursor()

        # Use the `the_darth_star` database
        cursor.execute("USE the_darth_star;")

        # Describe the structure of the `categories` table
        cursor.execute("DESCRIBE categories;")
        result = cursor.fetchall()

        # Expected table structure
        expected_structure = [
            ('id', 'int', 'NO', 'PRI', None, 'auto_increment'),
            ('name', 'varchar(100)', 'NO', '', None, ''),
            ('description', 'text', 'YES', '', None, '')
        ]

        # Check if the fetched structure matches the expected structure
        assert len(result) == len(expected_structure), f"Test Failed: 'categories' table has incorrect number of columns. Expected {len(expected_structure)}, got {len(result)}"

        for actual, expected in zip(result, expected_structure):
            assert actual[:6] == expected, f"Test Failed: Column {actual[0]} does not match the expected structure. Expected {expected}, got {actual[:6]}"

        print("Test Passed: 'categories' table structure is correct.")
    except Error as e:
        print(f"Test Failed: {e}")
    finally:
        close_connection(conn)

if __name__ == "__main__":
    database_name = "the_darth_star"  # Replace with your actual database name if different
    try:
        test_categories_table_exists()
        test_categories_table_structure()
    finally:
        # Clean up test data after tests are run
        cleanup_test_data(database_name, ["categories"])
