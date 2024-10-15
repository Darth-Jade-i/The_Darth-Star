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

    def tearDown(self):
        close_connection(self.conn, self.cursor)

    def test_create_user(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password_hash': 'hashed_password'
        }
        user_id = create_user(user_data)
        self.assertIsNotNone(user_id)

        # Verify the user was created
        self.cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user['username'], 'testuser')

    def test_read_user(self):
        # First, create a user
        user_data = {
            'username': 'readuser',
            'email': 'readuser@example.com',
            'password_hash': 'hashed_password'
        }
        user_id = create_user(user_data)

        # Now, read the user
        user = read_user(user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user['username'], 'readuser')

    def test_update_user(self):
        # First, create a user
        user_data = {
            'username': 'updateuser',
            'email': 'updateuser@example.com',
            'password_hash': 'hashed_password'
        }
        user_id = create_user(user_data)

        # Now, update the user
        updated_data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'password_hash': 'new_hashed_password'
        }
        result = update_user(user_id, updated_data)
        self.assertTrue(result)

        # Verify the update
        updated_user = read_user(user_id)
        self.assertEqual(updated_user['username'], 'updateduser')

    def test_delete_user(self):
        # First, create a user
        user_data = {
            'username': 'deleteuser',
            'email': 'deleteuser@example.com',
            'password_hash': 'hashed_password'
        }
        user_id = create_user(user_data)

        # Now, delete the user
        result = delete_user(user_id)
        self.assertTrue(result)

        # Verify the deletion
        deleted_user = read_user(user_id)
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()
