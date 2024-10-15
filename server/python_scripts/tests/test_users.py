import sys
import os
import unittest

# Add the directory containing db_handler.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from routes.users import create_user, read_user, update_user, delete_user
from db_handler import create_connection, close_connection


class TestUsersCRUD(unittest.TestCase):
    def setUp(self):
        self.conn = create_connection()
        self.cursor = self.conn.cursor(dictionary=True)

        # Clean up any existing test entries before each test
        test_emails = [
            'testuser@example.com',
            'readuser@example.com',
            'updateuser@example.com',
            'updateduser@example.com',
            'deleteuser@example.com'
        ]
        self.cursor.execute(
            'DELETE FROM users WHERE email IN (%s, %s, %s, %s, %s)',
            test_emails
        )
        self.conn.commit()

    def tearDown(self):
        # Clean up the database by deleting test entries based on email
        test_emails = [
            'testuser@example.com',
            'readuser@example.com',
            'updateuser@example.com',
            'updateduser@example.com',
            'deleteuser@example.com'
        ]
        self.cursor.execute(
            'DELETE FROM users WHERE email IN (%s, %s, %s, %s, %s)',
            test_emails
        )
        self.conn.commit()
        close_connection(self.conn, self.cursor)

    def test_create_user(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password_hash': 'hashed_password'
        }
        user_id = create_user(user_data)
        self.assertIsNotNone(user_id, "Failed to create user: user_id is None")

        # Verify the user was created
        self.cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user = self.cursor.fetchone()
        self.assertIsNotNone(user, f"Failed to fetch created user with id {user_id}")
        self.assertEqual(user['username'], 'testuser', f"Username mismatch: expected 'testuser', got {user['username']}")

    def test_read_user(self):
        user_data = {
            'username': 'readuser',
            'email': 'readuser@example.com',
            'password_hash': 'hashed_password'
        }
        user_id = create_user(user_data)
        self.assertIsNotNone(user_id, "Failed to create user for read test")

        user = read_user(user_id)
        self.assertIsNotNone(user, f"Failed to read user with id {user_id}")
        self.assertEqual(user['username'], 'readuser', f"Username mismatch: expected 'readuser', got {user['username']}")

    def test_update_user(self):
        user_data = {
            'username': 'updateuser',
            'email': 'updateuser@example.com',
            'password_hash': 'hashed_password'
        }
        user_id = create_user(user_data)
        self.assertIsNotNone(user_id, "Failed to create user for update test")

        updated_data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'password_hash': 'new_hashed_password'
        }
        result = update_user(user_id, updated_data)
        self.assertTrue(result, f"Failed to update user with id {user_id}")

        updated_user = read_user(user_id)
        self.assertIsNotNone(updated_user, f"Failed to read updated user with id {user_id}")
        self.assertEqual(updated_user['username'], 'updateduser', f"Username mismatch after update: expected 'updateduser', got {updated_user['username']}")

    def test_delete_user(self):
        user_data = {
            'username': 'deleteuser',
            'email': 'deleteuser@example.com',
            'password_hash': 'hashed_password'
        }
        user_id = create_user(user_data)
        self.assertIsNotNone(user_id, "Failed to create user for delete test")

        result = delete_user(user_id)
        self.assertTrue(result, f"Failed to delete user with id {user_id}")

        deleted_user = read_user(user_id)
        self.assertIsNone(deleted_user, f"User with id {user_id} still exists after deletion")

if __name__ == '__main__':
    unittest.main()

