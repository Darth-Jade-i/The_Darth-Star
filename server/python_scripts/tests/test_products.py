from db_handler import create_connection, close_connection
import sys
import os

# Add the directory containing db_handler.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_products_table_exists():
    """
    Tests whether the 'products' table exists in the database.
    """
    conn = create_connection()
    assert conn is not None, "Connection to MySQL database failed."

    cursor = conn.cursor()
    cursor.execute("SHOW TABLES LIKE 'products'")
    result = cursor.fetchone()

    assert result is not None, "Test Failed: 'products' table doesn't exist"
    close_connection(conn)


def test_products_table_structure():
    """
    Verifies that the structure of the 'products' table matches the expected structure.
    """
    conn = create_connection()
    assert conn is not None, "Connection to MySQL database failed."

    cursor = conn.cursor()
    cursor.execute("DESCRIBE products")
    columns = cursor.fetchall()

    expected_structure = [
        ('id', 'int', 'NO', 'PRI', None, 'auto_increment'),
        ('name', 'varchar(255)', 'NO', '', None, ''),
        ('description', 'text', 'YES', '', None, ''),
        ('price', 'decimal(10,2)', 'NO', '', None, ''),
        ('stock', 'int', 'YES', '', '0', ''),
        ('created_at', 'timestamp', 'YES', '', 'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED')
    ]

    for i, column in enumerate(columns):
        assert column[:6] == expected_structure[i], (
            f"Test Failed: Column {column[0]} does not match expected structure."
        )

    close_connection(conn)


if __name__ == "__main__":
    test_products_table_exists()
    test_products_table_structure()
    print("All tests passed for 'products' table.")
