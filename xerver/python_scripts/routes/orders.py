from db_handler import create_connection, close_connection
from mysql.connector import Error

def create_order(data):
    conn = create_connection()
    cursor = conn.cursor()
    query = '''
    INSERT INTO orders (user_id, product_id, quantity, total_price, status)
    VALUES (%s, %s, %s, %s, %s)
    '''
    try:
        cursor.execute(query, (
            data['user_id'],
            data['product_id'],
            data.get('quantity', 1),  # Use 1 as default if quantity is not provided
            data['total_price'],
            data.get('status', 'pending')  # Use 'pending' as default if status is not provided
        ))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return None
    finally:
        close_connection(conn, cursor)

def read_order(order_id):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    query = 'SELECT * FROM orders WHERE id = %s'
    try:
        cursor.execute(query, (order_id,))
        return cursor.fetchone()
    except Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        close_connection(conn, cursor)

def update_order(order_id, data):
    conn = create_connection()
    cursor = conn.cursor()
    query = '''
    UPDATE orders
    SET user_id = %s, product_id = %s, quantity = %s, total_price = %s, status = %s
    WHERE id = %s
    '''
    try:
        cursor.execute(query, (
            data.get('user_id'),
            data.get('product_id'),
            data.get('quantity'),
            data.get('total_price'),
            data.get('status'),
            order_id
        ))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return False
    finally:
        close_connection(conn, cursor)

def delete_order(order_id):
    conn = create_connection()
    cursor = conn.cursor()
    query = 'DELETE FROM orders WHERE id = %s'
    try:
        cursor.execute(query, (order_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return False
    finally:
        close_connection(conn, cursor)
