from db_handler import create_connection, close_connection
from mysql.connector import Error

def create_comment(data):
    conn = create_connection()
    cursor = conn.cursor()

    query = '''
    INSERT INTO comments (content, blog_id, user_id)
    VALUES (%s, %s, %s)
    '''

    try:
        cursor.execute(query, (data['content'], data['blog_id'], data['user_id']))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return None
    finally:
        close_connection(conn, cursor)

def read_comment(comment_id):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)

    query = 'SELECT * FROM comments WHERE id = %s'

    try:
        cursor.execute(query, (comment_id,))
        return cursor.fetchone()
    except Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        close_connection(conn, cursor)

def update_comment(comment_id, data):
    conn = create_connection()
    cursor = conn.cursor()

    query = '''
    UPDATE comments
    SET content = %s
    WHERE id = %s
    '''

    try:
        cursor.execute(query, (data['content'], comment_id))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return False
    finally:
        close_connection(conn, cursor)

def delete_comment(comment_id):
    conn = create_connection()
    cursor = conn.cursor()

    query = 'DELETE FROM comments WHERE id = %s'

    try:
        cursor.execute(query, (comment_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        return False
    finally:
        close_connection(conn, cursor)
