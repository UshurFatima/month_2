import sqlite3


def cities_list():
    with sqlite3.connect('hw_7.db') as connection:
        try:
            sql = '''SELECT id, title FROM cities'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(e)


def student_by_city(city_id):
    with sqlite3.connect('hw_7.db') as connection:
        try:
            sql = '''SELECT s.first_name, s.last_name, c.title, cit.title, cit.area FROM students as s
INNER JOIN cities as cit ON s.city_id = cit.id
INNER JOIN countries as c ON cit.country_id = c.id
WHERE cit.id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, city_id)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(e)


while True:
    print("Вы можете отобразить список учеников по выбранному id города из "
          "перечня городов ниже, для выхода из программы введите 0:")
    cities_list()
    city_id = input()
    if city_id == '0':
        break
    else:
        student_by_city(city_id)


