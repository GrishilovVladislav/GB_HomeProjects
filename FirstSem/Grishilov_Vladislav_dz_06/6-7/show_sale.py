FILENAME = 'bakery.csv'
p1 = 0
p2 = 0
from sys import argv
if len(argv) == 2:
  p1 = int(argv[1])
if len(argv) == 3:
  p1 = int(argv[1])
  p2 = int(argv[2])

def show_sale (num1 = 0, num2 = 0):
  with open (FILENAME, 'r', encoding='utf-8') as file:
    i = 1
    if num1 != 0:
      if num2 != 0:
        for line in file:
          if i >= num1 and i <= num2:
            print (line)
            if i > num2:
              return
          i = i + 1
      for line in file:
          if i >= num1:
            print (line)
          i = i + 1
    for line in file:
      print (line)

show_sale(p1,p2)