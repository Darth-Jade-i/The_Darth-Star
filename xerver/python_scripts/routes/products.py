from db_handler import create_connection, close_connection
from mysql.connector import Error

def create_product(data):
    conn = create_connection()
    cursor = conn.cursor()

    query = '''
    INSERT INTO products (name, description, price, stock)
    VALUES (%s, %s, %s, %s)
    '''

    try:
        cursor.execute(query, (data['name'], data['description'], data['price'], data['stock']))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return None
    finally:
        close_connection(conn, cursor)

def read_product(product_id):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    query = 'SELECT * FROM products WHERE id = %s'

    try:
        cursor.execute(query, (product_id,))
        return cursor.fetchone()
    except Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        close_connection(conn, cursor)

def update_product(product_id, data):
    conn = create_connection()
    cursor = conn.cursor()

    query = '''
    UPDATE products
    SET name = %s, description = %s, price = %s, stock = %s
    WHERE id = %s
    '''

    try:
        cursor.execute(query, (data['name'], data['description'], data['price'], data['stock'], product_id))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return False
    finally:
        close_connection(conn, cursor)

def delete_product(product_id):
    conn = create_connection()
    cursor = conn.cursor()

    query = 'DELETE FROM products WHERE id = %s'

    try:
        cursor.execute(query, (product_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return False
    finally:
        close_connection(conn, cursor)
