import sys
import os
import unittest

# Add the directory containing db_handler.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from products import create_product, read_product, update_product, delete_product
from db_handler import create_connection, close_connection

class TestProductsCRUD(unittest.TestCase):
    def setUp(self):
        self.conn = create_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def tearDown(self):
        close_connection(self.conn, self.cursor)

    def test_create_product(self):
        product_data = {
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': 100.00,
            'stock': 56
        }
        product_id = create_product(product_data)
        self.assertIsNotNone(product_id)

        # Verify the product was created
        self.cursor.execute('SELECT * FROM products WHERE id = %s', (product_id,))
        product = self.cursor.fetchone()
        self.assertIsNotNone(product)
        self.assertEqual(product['name'], 'Test Product')

    def test_read_product(self):
        # First, create a product
        product_data = {
            'name': 'Read Product',
            'description': 'This is a product for reading test',
            'price': 200.00,
            'stock': 100
        }
        product_id = create_product(product_data)

        # Now, read the product
        product = read_product(product_id)
        self.assertIsNotNone(product)
        self.assertEqual(product['name'], 'Read Product')

    def test_update_product(self):
        # First, create a product
        product_data = {
            'name': 'Update Product',
            'description': 'This is a product for updating test',
            'price': 300.00,
            'stock': 150
        }
        product_id = create_product(product_data)

        # Now, update the product
        updated_data = {
            'name': 'Updated Product',
            'description': 'This product has been updated',
            'price': 350.00,
            'stock': 200
        }
        result = update_product(product_id, updated_data)
        self.assertTrue(result)

        # Verify the update
        updated_product = read_product(product_id)
        self.assertEqual(updated_product['name'], 'Updated Product')

    def test_delete_product(self):
        # First, create a product
        product_data = {
            'name': 'Delete Product',
            'description': 'This is a product for deletion test',
            'price': 400.00,
            'stock': 50
        }
        product_id = create_product(product_data)

        # Now, delete the product
        result = delete_product(product_id)
        self.assertTrue(result)

        # Verify the deletion
        deleted_product = read_product(product_id)
        self.assertIsNone(deleted_product)

if __name__ == '__main__':
    unittest.main()
