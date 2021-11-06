FILENAME = 'bakery.csv'
from sys import argv
a = argv[1]
def add_sale (num):
  with open (FILENAME, 'a', encoding='utf-8') as file:
    file.write(str(num) + '\n')

add_sale(a)