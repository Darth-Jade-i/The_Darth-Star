import sys
import os
import unittest

# Add the directory containing python_scripts to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from routes.comments import create_comment, read_comment, update_comment, delete_comment
from routes.blogs import create_blog, delete_blog
from routes.users import create_user, delete_user

class TestComments(unittest.TestCase):
    def setUp(self):
        # Create a test user
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password_hash': 'testhash'
        }
        self.user_id = create_user(self.user_data)
        self.assertIsNotNone(self.user_id, "Failed to create test user")

        # Create a test blog
        self.blog_data = {
            'title': 'Test Blog',
            'content': 'This is a test blog post.',
            'author_id': self.user_id
        }
        self.blog_id = create_blog(self.blog_data)
        self.assertIsNotNone(self.blog_id, "Failed to create test blog")

        # Now create a test comment
        self.comment_data = {
            'content': 'This is a test comment.',
            'blog_id': self.blog_id,
            'user_id': self.user_id
        }
        self.comment_id = create_comment(self.comment_data)

    def tearDown(self):
        # Clean up: delete the comment, blog, and user
        if hasattr(self, 'comment_id'):
            delete_comment(self.comment_id)
        if hasattr(self, 'blog_id'):
            delete_blog(self.blog_id)
        if hasattr(self, 'user_id'):
            delete_user(self.user_id)

    def test_create_comment(self):
        self.assertIsNotNone(self.comment_id, "Failed to create comment")

    def test_read_comment(self):
        comment = read_comment(self.comment_id)
        self.assertIsNotNone(comment, f"Failed to read comment with id {self.comment_id}")
        self.assertEqual(comment['content'], self.comment_data['content'])

    def test_update_comment(self):
        updated_data = {'content': 'Updated test comment'}
        result = update_comment(self.comment_id, updated_data)
        self.assertTrue(result, f"Failed to update comment with id {self.comment_id}")

        # Verify the update
        updated_comment = read_comment(self.comment_id)
        self.assertEqual(updated_comment['content'], updated_data['content'])

    def test_delete_comment(self):
        result = delete_comment(self.comment_id)
        self.assertTrue(result, f"Failed to delete comment with id {self.comment_id}")

        # Verify the deletion
        deleted_comment = read_comment(self.comment_id)
        self.assertIsNone(deleted_comment, f"Comment with id {self.comment_id} still exists after deletion")

if __name__ == '__main__':
    unittest.main()
