import sqlite3

db_connect = sqlite3.connect('d13.sqlite3')
db_cursor = db_connect.cursor()


async def db_get_all_products():
    products = db_cursor.execute("""
        SELECT * FROM product
    """).fetchall()
    return products


async def db_create_product(title, price, photo):
    product = db_cursor.execute("""
        INSERT INTO product (title, price, photo) VALUES (?, ?, ?)
    """, (title, price, photo))
    db_connect.commit()
    return product
