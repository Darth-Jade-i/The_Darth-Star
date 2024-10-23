import sys
import os
import mysql.connector
from mysql.connector import Error

# Add the directory containing db_handler.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_handler import create_connection, close_connection

def test_orders_table_exists():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES LIKE 'orders'")
    result = cursor.fetchone()
    assert result is not None, "Test Failed: 'orders' table doesn't exist"
    print("Test Passed: 'orders' table exists")
    close_connection(connection)

def test_orders_table_structure():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DESCRIBE orders")
    columns = cursor.fetchall()

    # Expected structure of the 'orders' table
    expected_structure = [
        ('id', 'int', 'NO', 'PRI', None, 'auto_increment'),
        ('user_id', 'int', 'YES', 'MUL', None, None),
        ('product_id', 'int', 'YES', 'MUL', None, None),
        ('quantity', 'int', 'YES', None, '1', None),
        ('total_price', 'decimal(10,2)', 'NO', None, None, None),
        ('created_at', 'timestamp', 'YES', None, 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED')
    ]

    # Check if the actual structure matches the expected structure
    for i, column in enumerate(columns):
        assert column[:6] == expected_structure[i], (
            f"Test Failed: Column {column[0]} does not match expected structure."
        )

    print("Test Passed: 'orders' table structure is correct")
    close_connection(connection)

# Run the tests
if __name__ == "__main__":
    try:
        test_orders_table_exists()
        test_orders_table_structure()
    except AssertionError as e:
        print(e)
