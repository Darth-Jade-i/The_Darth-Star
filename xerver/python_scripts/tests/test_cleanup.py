import mysql.connector
from mysql.connector import Error
import sys
import os

# Add the directory containing db_handler.py to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import db_config

def cleanup_test_data(database_name, tables=None):
    """
    Cleans up test data from specified tables or all tables in the given database.
    
    :param database_name: Name of the database to clean up
    :param tables: List of table names to clean up. If None, cleans all tables.
    """
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Use the specified database
        cursor.execute(f"USE {database_name};")

        # Disable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

        # If no specific tables are provided, get all tables in the database
        if tables is None:
            cursor.execute("SHOW TABLES;")
            tables = [table[0] for table in cursor.fetchall()]

        # Clean up each table
        for table in tables:
            try:
                print(f"Cleaning up table: {table}")
                cursor.execute(f"DELETE FROM {table};")
                cursor.execute(f"ALTER TABLE {table} AUTO_INCREMENT = 1;")
            except Error as e:
                print(f"Error cleaning up table {table}: {e}")

        # Re-enable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

        connection.commit()
        print("Test data cleanup completed successfully.")

    except Error as e:
        print(f"Error during cleanup: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    # You can run this script directly to clean up all tables
    database_name = "the_darth_star"  # Replace with your database name
    cleanup_test_data(database_name)

    # Or you can specify tables to clean up
    # specific_tables = ["categories", "products", "users"]
    # cleanup_test_data(database_name, specific_tables)
