import sys
import os
import unittest

# Add the directory containing db_handler.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from routes.orders import create_order, read_order, update_order, delete_order
from db_handler import create_connection, close_connection


class TestOrders(unittest.TestCase):
    def setUp(self):
        # Create a test order
        self.order_data = {
            'user_id': 1,
            'product_id': 1,
            'quantity': 2,
            'total_price': 19.99,
            'status': 'pending'
        }
        self.order_id = create_order(self.order_data)

    def test_create_order(self):
        self.assertIsNotNone(self.order_id)

    def test_read_order(self):
        order = read_order(self.order_id)
        self.assertIsNotNone(order)
        self.assertEqual(order['user_id'], self.order_data['user_id'])
        self.assertEqual(order['product_id'], self.order_data['product_id'])
        self.assertEqual(order['quantity'], self.order_data['quantity'])
        self.assertEqual(float(order['total_price']), self.order_data['total_price'])
        self.assertEqual(order['status'], self.order_data['status'])

    def test_update_order(self):
        update_data = {
            'user_id': 2,
            'product_id': 2,
            'quantity': 3,
            'total_price': 29.99,
            'status': 'processing'
        }
        result = update_order(self.order_id, update_data)
        self.assertTrue(result)
        updated_order = read_order(self.order_id)
        self.assertEqual(updated_order['user_id'], update_data['user_id'])
        self.assertEqual(updated_order['product_id'], update_data['product_id'])
        self.assertEqual(updated_order['quantity'], update_data['quantity'])
        self.assertEqual(float(updated_order['total_price']), update_data['total_price'])
        self.assertEqual(updated_order['status'], update_data['status'])

    def test_delete_order(self):
        result = delete_order(self.order_id)
        self.assertTrue(result)
        deleted_order = read_order(self.order_id)
        self.assertIsNone(deleted_order)

    def tearDown(self):
        # Clean up any remaining test data
        delete_order(self.order_id)

if __name__ == '__main__':
    unittest.main()
