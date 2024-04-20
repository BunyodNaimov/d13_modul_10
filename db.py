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


def create_table_product():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY,
        title TEXT,
        price REAL,
        photo TEXT)
    """)


async def db_insert_product(title, price, photo_id):
    db_cursor.execute("""
            INSERT INTO product (title, price, photo)
            VALUES(?, ?, ?)""", (title, price, photo_id))
    db_connect.commit()


async def db_get_all_products():
    products = db_cursor.execute("""
        SELECT * FROM product
    """).fetchall()
    return products


def create_table_orders():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        user_id INTEGER)
    """)


async def insert_orders(product_id, user_id):
    db_cursor.execute("""
            INSERT INTO orders (product_id, user_id)
            VALUES(?, ?)""", (product_id, user_id))
    db_connect.commit()


async def db_get_all_orders(user_id):
    orders = db_cursor.execute("""
        SELECT * FROM orders WHERE user_id=?
    """, (user_id,)).fetchall()

    products = []
    for order in orders:
        product = db_cursor.execute("""
        SELECT * FROM product WHERE id=?
        """, (order[1],)).fetchone()

        products.append(product)

    user = db_cursor.execute("""
        SELECT * FROM users WHERE telegram_id=?
    """, (user_id,)).fetchone()
    return user, products


def db_create_favorites():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites(
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_id INTEGER)
    """)
    db_connect.commit()


async def db_insert_favorites(user_id, product_id):
    db_cursor.execute("""
        INSERT INTO favorites(user_id, product_id) VALUES(?, ?)
    """, (user_id, product_id))
    db_connect.commit()


async def db_get_all_favorites(user_id):
    favorites = db_cursor.execute("""
        SELECT * FROM favorites WHERE user_id=?
    """, (user_id,)).fetchall()

    products = []
    if not favorites:
        return products

    for favorite in favorites:
        product = db_cursor.execute("""
            SELECT * FROM product WHERE product.id=?
        """, (favorite[2],)).fetchone()
        products.append(product)

    return products

