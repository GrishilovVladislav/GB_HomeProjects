FILENAME = 'nginx_logs.txt'
result = []
with open (FILENAME, 'r') as file:
  for line in file:
    line_list = line.split()
    result.append((line_list[0],line_list[5][1:],line_list[6]))
#Если структура файла остается прежней, то подойдет и такой вариант 