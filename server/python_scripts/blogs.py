from db_handler import create_connection, close_connection
from mysql.connector import Error

def create_blog(data):
    conn = create_connection()
    cursor = conn.cursor()

    query = '''
    INSERT INTO blogs (title, content, author_id)
    VALUES (%s, %s, %s)
    '''

    try:
        cursor.execute(query, (data['title'], data['content'], data['author_id']))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return None
    finally:
        close_connection(conn, cursor)

def read_blog(blog_id):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    query = 'SELECT * FROM blogs WHERE id = %s'

    try:
        cursor.execute(query, (blog_id,))
        return cursor.fetchone()
    except Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        close_connection(conn, cursor)

def update_blog(blog_id, data):
    conn = create_connection()
    cursor = conn.cursor()

    query = '''
    UPDATE blogs
    SET title = %s, content = %s
    WHERE id = %s
    '''

    try:
        cursor.execute(query, (data['title'], data['content'], blog_id))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return False
    finally:
        close_connection(conn, cursor)

def delete_blog(blog_id):
    conn = create_connection()
    cursor = conn.cursor()

    query = 'DELETE FROM blogs WHERE id = %s'

    try:
        cursor.execute(query, (blog_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return False
    finally:
        close_connection(conn, cursor)
