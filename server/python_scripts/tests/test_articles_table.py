from db_handler import create_connection, close_connection
import sys
import os
import mysql.connector
from mysql.connector import Error
# Add the parent directory to the Python path to access db_handler.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_articles_table_exists():
    """Test if the 'articles' table exists in the 'the_darth_star' database."""
    conn = create_connection()
    if conn is None:
        print("Test Failed: Unable to establish a connection to the database.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("USE the_darth_star;")
        cursor.execute("SHOW TABLES LIKE 'articles';")
        result = cursor.fetchone()
        assert result is not None, "Test Failed: 'articles' table doesn't exist"
        print("Test Passed: 'articles' table exists")
    except Error as e:
        print(f"Test Failed: {e}")
    finally:
        close_connection(conn)


def test_articles_table_structure():
    """Test if the 'articles' table has the expected structure."""
    conn = create_connection()
    if conn is None:
        print("Test Failed: Unable to establish a connection to the database.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("USE the_darth_star;")
        cursor.execute("DESCRIBE articles;")
        result = cursor.fetchall()
        print("Actual table structure:")
        for column in result:
            print(column)

        # Updated expected table structure
        expected_structure = [
            ('id', 'int', 'NO', 'PRI', None, 'auto_increment'),
            ('title', 'varchar(255)', 'NO', '', None, ''),
            ('content', 'text', 'NO', '', None, ''),
            ('author', 'varchar(100)', 'NO', '', None, ''),
            ('created_at', 'datetime', 'YES', '',
             'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED'),
            ('updated_at', 'datetime', 'YES', '', 'CURRENT_TIMESTAMP',
             'DEFAULT_GENERATED on update CURRENT_TIMESTAMP')
        ]
        # Check if the fetched structure matches the expected structure
        for i, column in enumerate(result):
            assert column[:6] == expected_structure[i], (
                f"Test Failed: Column {
                    column[0]} does not match the expected structure."
            )
            print("Test Passed: 'articles' table structure is correct.")
    except Error as e:
        print(f"Test Failed: {e}")
    finally:
        close_connection(conn)


if __name__ == "__main__":
    test_articles_table_exists()
    test_articles_table_structure()
