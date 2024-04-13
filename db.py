import sqlite3

db_connect = sqlite3.connect('d13.sqlite3')

db_cursor = db_connect.cursor()


def create_users():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, full_name TEXT, phone TEXT, telegram_id INTEGER
        )
    """)
    db_connect.commit()


async def insert_user(full_name, phone, telegram_id):
    db_cursor.execute("""
        INSERT INTO users (full_name, phone, telegram_id)
        VALUES(?, ?, ?)""", (full_name, phone, telegram_id))
    db_connect.commit()


def delete_users():
    db_cursor.execute("""
        DELETE FROM users WHERE  id=1
    """)
    db_connect.commit()


def update_users():
    db_cursor.execute("""
        UPDATE users SET last_name='DOE', first_name='JON' WHERE id=2
    """)
    db_connect.commit()


def drop_users():
    db_cursor.execute("""
        DROP TABLE users
    """)


def create_table_product():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY,
        title TEXT,
        price REAL,
        photo TEXT)
    """)


def create_table_orders():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        user_id INTEGER)
    """)


def update_users():
    db_cursor.execute("""
        UPDATE users SET first_name = 'Jon', last_name = 'Doe' WHERE id=1
    """)


def delete_users():
    db_cursor.execute(
        "DROP TABLE users"
    )
    # db_cursor.execute("""
    #     DELETE FROM users WHERE id=1
    # """)


async def db_insert_product(title, price, photo_id):
    db_cursor.execute("""
            INSERT INTO product (title, price, photo)
            VALUES(?, ?, ?)""", (title, price, photo_id))
    db_connect.commit()


def insert_orders(product_id, user_id):
    db_cursor.execute("""
            INSERT INTO orders (product_id, user_id)
            VALUES(?, ?)""", (product_id, user_id))


def db_get_all_products():
    products = db_cursor.execute("""
        SELECT * FROM product
    """).fetchall()
    return products
