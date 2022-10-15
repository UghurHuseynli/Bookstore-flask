import pymysql.cursors
import sys
import os
# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='windwalker',
                             database='project_db',
                             cursorclass=pymysql.cursors.DictCursor)

op = ''
try:
    input_ = sys.argv
    op = ' '.join(input_[1:])
except:
    print("\nPlease enter correct operation...\n")


def create_table():
    with connection.cursor() as cursor:
        sql = """Create table if not exists Book_info(id int unsigned primary key AUTO_INCREMENT,
                        title varchar(100),
                        author varchar(50),
                        published_at date,
                        is_exist boolean,
                        genre varchar(50),
                        language varchar(30),
                        price int);"""
        cursor.execute(sql)
    connection.commit()
    print('\nTable was create !\n')


def create_book(input_1):
    try:
        with connection.cursor() as cursor:
            sql = "Insert into Book_info(title,author,published_at, is_exist, genre,language,price) VALUES (%s, %s, %s, 0, %s, %s, %s)"
            cursor.execute(
                sql, (input_1[0], input_1[1], input_1[2], input_1[3], input_1[4], input_1[5]))
        connection.commit()
        print('\nBook was added to the table\n')
    except:
        print('\nPlease first create table\n')


def show_all():
    try:
        with connection.cursor() as cursor:
            sql = "select * from Book_info"
            cursor.execute(sql)
            result = cursor.fetchall()
        if result == ():
            print('\nTable is empty\n')
        else:
            for books in result:
                for key, value in books.items():
                    print(f'{key} : {value}')
                print()
    except:
        print('\nPlease first create table\n')


def show_book(id_):
    try:
        with connection.cursor() as cursor:
            sql = 'select * from Book_info where id = %s'
            cursor.execute(sql, (id_,))
        book = cursor.fetchone()
        for key, value in book.items():
            print(f'{key} : {value}')
    except:
        print('\nPlease first create table\n')


def change_status(id):
    with connection.cursor() as cursor:
        sql = 'Update Book_info set is_exist = not is_exist where id = %s'
        cursor.execute(sql, (id,))
    connection.commit()
    print('\nStatus was changed...\n')


def change_price(id, price):
    with connection.cursor() as cursor:
        sql = 'Update Book_info set price = %s where id = %s'
        cursor.execute(sql, (price, id))
    connection.commit()
    print('\nPrice was changed...\n')


def remove(id):
    with connection.cursor() as cursor:
        sql = 'Delete from Book_info where id = %s'
        cursor.execute(sql, (id,))
    connection.commit()
    print('\nBook was deleted...\n')


def search(like):
    with connection.cursor() as cursor:
        sql = f"Select * from Book_info where title LIKE '%{like}%' or author LIKE '%{like}%'"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            for books in result:
                for key, value in books.items():
                    print(f'{key} : {value}')
                print()
        else:
            print('\nThe book was not found\n')


if op == 'add table':
    create_table()

elif op == 'add book':
    input_1 = input(
        '\nPlease enter the book field as follows: title author published_at(YYYY-MM-DD) genre language price:  ')
    fields_sect = input_1.split()
    if len(fields_sect) == 6:
        create_book(fields_sect)
    else:
        print('\nPlease enter correct input.')
        os.system('python Python\day_25.py add book')

elif op == 'show all':
    show_all()

elif op == 'show book':
    id_ = input('\nPlease enter book id: \n')
    if id_:
        show_book(id_)
    else:
        print('\nEnter the id of the book you want to find')
        os.system('python Python\day_25.py show book')

elif op == 'change status':
    id_ = input('\nPlease enter book id: \n')
    if id_:
        change_status(id_)
    else:
        print('\nEnter the id of the book you want to change')
        os.system('python Python\day_25.py change status')

elif op == 'change price':
    id_ = input('\nPlease enter book id: \n')
    price = input('\nPlease enter new price: \n')
    if id_ and price:
        change_price(id_, price)
    else:
        print('\nEnter the id of the book you want to change')
        os.system('python Python\day_25.py change price')

elif op == 'remove':
    id = input('\nPlease enter book id: \n')
    if id:
        remove(id)
    else:
        print('\nEnter the id of the book you want to remove')
        os.system('python Python\day_25.py remove')

elif op == 'search':
    like = input('\nPlease enter search word: ')
    if like:
        search(like)
    else:
        print('\nEnter the search word')
        os.system('python Python\day_25.py search')

else:
    print('\nPlease enter correct operation...\n')
