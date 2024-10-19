import sys
import os

# Add the directory containing db_handler.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_handler import create_connection, close_connection


def test_blogs_table_exists():
    conn = create_connection()
    assert conn is not None, "Connection to MySQL database failed."

    cursor = conn.cursor()
    cursor.execute("SHOW TABLES LIKE 'blogs'")
    result = cursor.fetchone()

    assert result is not None, "Test Failed: 'blogs' table doesn't exist"

    close_connection(conn)


def test_blogs_table_structure():
    conn = create_connection()
    assert conn is not None, "Connection to MySQL database failed."

    cursor = conn.cursor()
    cursor.execute("DESCRIBE blogs")
    columns = cursor.fetchall()

    expected_structure = [
        ('id', 'int', 'NO', 'PRI', None, 'auto_increment'),
        ('title', 'varchar(255)', 'NO', '', None, ''),
        ('content', 'text', 'NO', '', None, ''),
        ('author_id', 'int', 'YES', 'MUL', None, ''),
        ('created_at', 'timestamp', 'YES', '',
         'CURRENT_TIMESTAMP', 'DEFAULT_GENERATED')
    ]

    for i, column in enumerate(columns):
        assert column[:6] == expected_structure[i], (
            f"Test Failed: Column {
                column[0]} does not match expected structure."
        )

    close_connection(conn)


if __name__ == "__main__":
    test_blogs_table_exists()
    test_blogs_table_structure()
    print("All tests passed for 'blogs' table.")
