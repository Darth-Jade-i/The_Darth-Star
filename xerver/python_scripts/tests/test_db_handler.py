import sys
import os


# Add the directory containing db_handler.py to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_failed_connection():
    """Test for connection failure with incorrect credentials."""
    from db_handler import create_connection

    # Temporarily change the connection parameters to simulate a failure.
    incorrect_params = {
        "host": "localhost",
        "user": "wrong_user",
        "password": "wrong_password",
        "database": "non_existent_db"
    }

    try:
        connection = create_connection(**incorrect_params)
        if connection:
            print("Unexpected success: Test failed")
        else:
            print("Connection failed as expected: Test passed")
    except Exception as e:
        print(f"Handled failed connection properly: {e}")


def test_close_connection():
    """Test closing a connection."""
    from db_handler import create_connection, close_connection

    connection = create_connection()
    try:
        # Try closing an active connection.
        if connection:
            close_connection(connection)
            print("Connection closed successfully: Test passed")
        else:
            print("Connection was not established: Test failed")

        # Try closing an already closed connection.
        close_connection(connection)
        print("No error when closing already closed connection: Test passed")
    except Exception as e:
        print(f"Error when closing connection: {e}")


def test_create_database():
    """Test creating a new database."""
    from db_handler import create_connection, close_connection

    connection = create_connection()
    try:
        if connection:
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS test_db;")
            print("Database created or already exists: Test passed")
        else:
            print("No connection for database creation: Test failed")
    except Exception as e:
        print(f"Error creating database: {e}")
    finally:
        if connection:
            # Drop the test database to clean up after the test
            cursor.execute("DROP DATABASE IF EXISTS test_db;")
            close_connection(connection)
            print("Test database dropped successfully.")
