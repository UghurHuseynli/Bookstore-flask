import sys, os
from datetime import datetime


class Book():
    def __init__(self, title, author, id, date):
        self.title = title 
        self.author = author
        self.id = id
        self.date = date

    def set_date(self):
        return datetime.today().strftime("%d %B %Y")

    def set_id(self, obj):
        with open('File/file.txt', 'r+', encoding='utf-8') as file:
            last_id = 1
            if obj:
                last_id = int(obj[-5].split(':')[1]) + 1
            return last_id

    def add_(self, tit, wrt):
        if tit and wrt:
            with open('File/file.txt', 'r+', encoding='utf-8') as file:
                obj = file.readlines()
                ele = f'ID : {self.set_id(obj)}\nBook name : {tit}\nWriter name : {wrt}\nAdded in : {self.set_date()}'
                file.write(f"{ele}\n{'*' * 50}\n")
            print('\nBook was added\n')
        else:
            print('\nPlease enter correct input\n')

    def show_all(self, myobj):
        if myobj:
            print('*' * 50)
            print(*myobj, sep='\n')
        else:
            print('\nList is empty\n')

    def show_book(self, my_id, my_obj):
        for i in range(0, len(my_obj), 5):
            search = my_obj[i].split(':')[1].strip()
            if my_id == search:
                print('*' * 50)
                for j in range(i, i + 5):
                    print(my_obj[j])
                return
        print('\nId not found\n')
    
    def remove(self, my_rem_id):
        with open('File/file.txt', 'r+', encoding='utf-8') as file:
            lists = file.readlines()
            file.seek(0)
            index = -1
            for line in range(0, len(lists), 5):
                remove_ele = lists[line].split(':')[1].strip()
                if my_rem_id == remove_ele:
                    index = line
                    break
            else:
                print('\nId not found\n')
                return
            if index != -1:
                number_list = [index, index + 1, index + 2, index + 3, index + 4]
                file.truncate()
                for i in range(len(lists)):
                    if i not in number_list:
                        file.write(lists[i])
                print('\nBook was deleted...\n')


def do_operation(op):
    is_exists = os.path.exists('.\File')
    if not is_exists:
        os.mkdir('.\File')

    with open('File\\file.txt', 'a+', encoding='utf-8') as file:
        file.seek(0)
        obj = file.readlines()

    mybook = Book('lazimsiz', 'lazimsiz', -111, '1.1.1.1')

    if op == 'show all':
        mybook.show_all(obj)

    elif op == 'add':
        title = input('Enter book name: ')
        writer = input('Enter writer name: ')
        mybook.add_(title, writer)

    elif op == 'show book':
        show_id = input('Enter book id: ')
        mybook.show_book(show_id, obj)

    elif op == 'remove':
        remove_id = input('Enter book id: ')
        mybook.remove(remove_id)
    else:
        print('\nWrong operation\n')



input_ = sys.argv
if len(input_) >= 2:
    operation = ' '.join(input_[1:])
    do_operation(operation)
else:
    print('\nPlease select the action you want to do\n')