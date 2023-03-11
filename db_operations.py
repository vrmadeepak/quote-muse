import sqlite3

def get_conn():
    return sqlite3.connect("db.sqlite3")

def create_tables():
    con = get_conn()
    cur = con.cursor()

    # python validation for phone or email - one to be entered
    user_create_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            username VARCHAR(50) UNIQUE, 
            first_name VARCHAR(50), 
            last_name VARCHAR(50), 
            phone VARCHAR(20), 
            email VARCHAR(100)
        )
    '''
    cur.execute(user_create_query)
    cur.close()

    quote_create_query = '''
        CREATE TABLE IF NOT EXISTS quotes (
            id AUTO_INCREMENT PRIMARY KEY, 
            user_id INT, 
            author VARCHAR(50), 
            quote TEXT, 
            category VARCHAR(50), 
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    '''
    cur = con.cursor()
    cur.execute(quote_create_query)
    cur.close()

    con.close()

def get_user(username, communication=None):
    con = get_conn()
    cur = con.cursor()

    if communication:
        query = f'''SELECT * from users 
            where username='{username}' and (phone = '{communication}' or email='{communication}');'''
    else: 
        query = f'''SELECT id, username, first_name, last_name, phone, email from users where username='{username}';'''
    cur.execute(query)
    user = cur.fetchall()
    cur.close()
    con.close()
    return user

def add_user(username, first_name, last_name, phone, email):
    con = get_conn()
    cur = con.cursor()

    query = f'''INSERT INTO users 
        (username, first_name, last_name, phone, email)
        VALUES ('{username}', '{first_name}', '{last_name}', '{phone}', '{email}');'''
    cur.execute(query)
    cur.close()
    con.commit()
    con.close()
    print('User successfully Added!')
    return 
