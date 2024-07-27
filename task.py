import sqlite3


def show_stores(db_name):
    with sqlite3.connect(db_name) as connection:
        try:
            sql = '''SELECT * FROM store'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        except sqlite3.Error:
            print(sqlite3.Error)


def products_by_store(db_name, store_id):
    with sqlite3.connect(db_name) as connection:
        try:
            sql = '''SELECT p.title, c.title, p.unit_price, p.stock_quantity FROM products as p
INNER JOIN categories as c ON p.category_code == c.code
INNER JOIN store as s ON p.store_id == s.store_id
where s.store_id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, store_id)
            rows = cursor.fetchall()
            for row in rows:
                print(f'Название продукта: {row[0]}')
                print(f'Категория: {row[1]}')
                print(f'Цена: {row[2]} ')
                print(f'Количество на складе: {row[3]} ')
                print('--------------')
        except sqlite3.Error:
            print(sqlite3.Error)


while True:
    print('Вы можете отобразить список продуктов по выбранному id магазина из '
          'перечня магазинов ниже, для выхода из программы введите цифру 0:')
    show_stores('test.db')
    store_id = input()
    if store_id == '0':
        break
    products_by_store('test.db', store_id)
