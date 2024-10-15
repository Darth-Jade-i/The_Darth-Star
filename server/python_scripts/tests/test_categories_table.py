import mysql.connector
import sys
import os
from mysql.connector import Error

# Add the directory containing db_handler.py to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
            ('created_at', 'timestamp', 'YES', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED')
        ]
        
        assert len(columns) == len(expected_columns), "Test Failed: 'categories' table has incorrect number of columns"
        
        for actual, expected in zip(columns, expected_columns):
            assert actual[:6] == expected, f"Test Failed: Column {actual[0]} does not match expected structure"
        
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
            ('created_at', 'timestamp', 'YES', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED')
        ]
        
        # Check if the fetched structure matches the expected structure
        for i, column in enumerate(result):
            assert column[:6] == expected_structure[i], (
                f"Test Failed: Column {column[0]} does not match the expected structure."
            )
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
