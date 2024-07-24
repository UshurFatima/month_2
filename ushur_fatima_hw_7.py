import sqlite3

try:
    sqlite3.connect('''hw.db''')
except sqlite3.Error as e:
    print(e)

sql_to_create_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''


def create_table(db_name):
    with sqlite3.connect(db_name) as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(sql_to_create_table)
        except sqlite3.Error as e:
            print(e)


def insert_product(db_name):
    with sqlite3.connect(db_name) as connection:
        try:
            sql_to_insert_product = '''
            INSERT INTO products (product_title, price, quantity) 
            VALUES ('Альбом', 150.0, 20), ('Краски акварельные', 300.5, 15),
            ('Краски акриловые', 200.5, 25), ('Краски масляные', 330.3, 19),
            ('Гуашь', 120.0, 30), ('Кисти синтетические', 80.0, 20),
            ('Кисти из шерсти', 170.7, 25), ('Карандаши цветные', 400.0, 30),
            ('Карандаши простые', 20.0, 40), ('Мальберт', 370.5, 22),
            ('Холст', 200.0, 24), ('Палитра', 170.4, 45),
            ('Мастихин', 310.1, 28), ('Резинки', 50.6, 40),
            ('Клячки', 40.4, 40)'''
            cursor = connection.cursor()
            cursor.execute(sql_to_insert_product)
            connection.commit()
        except sqlite3.Error as e:
            print(e)


def change_quantity(db_name, product):
    with sqlite3.connect(db_name) as connection:
        try:
            sql = '''UPDATE products SET quantity = ?
                        WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as e:
            print(e)


def change_price(db_name, product):
    with sqlite3.connect(db_name) as connection:
        try:
            sql = '''UPDATE products SET price = ?
                        WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as e:
            print(e)


def delete_product(db_name, id):
    with sqlite3.connect(db_name) as connection:
        try:
            sql = '''DELETE FROM products WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
        except sqlite3.Error as e:
            print(e)


def select_products(db_name):
    with sqlite3.connect(db_name) as connection:
        try:
            sql = '''SELECT * FROM products'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(e)


def products_by_price_and_quantity(db_name):
    with sqlite3.connect(db_name) as connection:
        try:
            sql = '''SELECT * FROM products WHERE price < 100 and quantity > 5'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(e)


def find_products_by_name(db_name, word):
    with sqlite3.connect(db_name) as connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", (word, ))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(e)


# create_table('hw.db')
# insert_product('hw.db')
# change_quantity('hw.db', (30, 7))
# change_price('hw.db', (250.6, 2))
# delete_product('hw.db', 5)
# select_products('hw.db')
# products_by_price_and_quantity('hw.db')
find_products_by_name('hw.db', 'Краски')

