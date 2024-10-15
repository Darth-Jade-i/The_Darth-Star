from mysql.connector import Error
from db_handler import create_connection, close_connection

def create_user(data):
    conn = create_connection()
    cursor = conn.cursor()
    query = '''
    INSERT INTO users (username, email, password_hash)
    VALUES (%s, %s, %s)
    '''
    try:
        print(f"Attempting to insert user: {data}")
        cursor.execute(query, (data['username'], data['email'], data['password_hash']))
        conn.commit()
        user_id = cursor.lastrowid
        print(f"User created with ID: {user_id}")
        return user_id
    except Error as e:
        print(f"An error occurred while creating user: {e}")
        conn.rollback()
        return None
    finally:
        close_connection(conn, cursor)

def read_user(user_id):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    query = 'SELECT * FROM users WHERE id = %s'
    try:
        print(f"Attempting to read user with ID: {user_id}")
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        print(f"Read user: {user}")
        return user
    except Error as e:
        print(f"An error occurred while reading user: {e}")
        return None
    finally:
        close_connection(conn, cursor)

def update_user(user_id, data):
    conn = create_connection()
    cursor = conn.cursor()
    query = '''
    UPDATE users
    SET username = %s, email = %s, password_hash = %s
    WHERE id = %s
    '''
    try:
        print(f"Attempting to update user {user_id} with data: {data}")
        cursor.execute(query, (data['username'], data['email'], data['password_hash'], user_id))
        conn.commit()
        success = cursor.rowcount > 0
        print(f"Update user result: {'Success' if success else 'Failed'}")
        return success
    except Error as e:
        print(f"An error occurred while updating user: {e}")
        conn.rollback()
        return False
    finally:
        close_connection(conn, cursor)

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    query = 'DELETE FROM users WHERE id = %s'
    try:
        print(f"Attempting to delete user with ID: {user_id}")
        cursor.execute(query, (user_id,))
        conn.commit()
        success = cursor.rowcount > 0
        print(f"Delete user result: {'Success' if success else 'Failed'}")
        return success
    except Error as e:
        print(f"An error occurred while deleting user: {e}")
        conn.rollback()
        return False
    finally:
        close_connection(conn, cursor)

def get_user_by_email(email):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    query = 'SELECT * FROM users WHERE email = %s'
    try:
        print(f"Attempting to get user with email: {email}")
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        print(f"Retrieved user: {user}")
        return user
    except Error as e:
        print(f"An error occurred while getting user by email: {e}")
        return None
    finally:
        close_connection(conn, cursor)
