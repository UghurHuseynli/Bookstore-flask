import sys
from datetime import datetime

operation = sys.argv

if '-' in operation:
    index = operation.index('-')
    if(len(operation[:index]) >= 2 and len(operation[index + 1:]) >= 1 ):
        print(f'Book name: {" ".join(operation[1:index])}\nWriter: {" ".join(operation[index + 1:])}\nAdded in: {datetime.now().strftime("%d %B %Y")}')
    else:
        print('Wrong input format. Please enter the correct input!!!')
else:
    print('Wrong input format. Please enter the correct input!!!')