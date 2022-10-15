import sys, os
from datetime import datetime

def no_book(func):
    def wrapping(*args):
        obj = args[0]
        if obj:
            func(obj)
        else:
            print('List is empty')
    return wrapping


def add_(title, writer):
    if title and writer:
        with open('File/file_1.txt', 'r+', encoding='utf-8') as file:
            obj = file.readlines()
            last_id = 1
            if obj:
                last_id = int(obj[-5].split(':')[1]) + 1
            ele = f'ID : {last_id}\nBook name : {title}\nWriter name : {writer}\nAdded in : {datetime.today().strftime("%d %B %Y")}'
            file.write(f"{ele}\n{'*' * 50}\n")
        return True
    else:
        return False


@no_book
def show_all(list_):
    print('*' * 50)
    print(*list_, sep='\n')


def show_book(id, obj):
    for i in range(0, len(obj), 5):
        search = obj[i].split(':')[1].strip()
        if id == search:
            print('*' * 50)
            for j in range(i, i + 5):
                print(obj[j])
            return True
    return False


def remove_(id):
    with open('File/file_1.txt', 'r+', encoding='utf-8') as file:
        lists = file.readlines()
        file.seek(0)
        index = -1
        for line in range(0, len(lists), 5):
            remove_ele = lists[line].split(':')[1].strip()
            if id == remove_ele:
                index = line
                break
        else:
            print('\nId not found\n')
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

    with open('.\File\\file_1.txt', 'a+', encoding='utf-8') as file:
        file.seek(0)
        obj = file.readlines()
    
    if op == 'show all':
        show_all(obj)
    elif op == 'add':
        title = input('Enter book name: ')
        writer = input('Enter writer name: ')
        result_add = add_(title, writer)
        if result_add:
            print('\nBook was added...\n')
        else:
            print('\nPlease enter correct input\n')
    elif op == 'show book':
        show_id = input('Enter book id: ')
        result_show = show_book(show_id, obj)
        if not result_show:
            print('Id not found')
    elif op == 'remove':
        remove_id = input('Enter book id: ')
        remove_(remove_id)
    else:
        print('Wrong operation')

input_ = sys.argv
if len(input_) >= 2:
    operation = ' '.join(input_[1:])
    do_operation(operation)
else:
    print('Please select the action you want to do')