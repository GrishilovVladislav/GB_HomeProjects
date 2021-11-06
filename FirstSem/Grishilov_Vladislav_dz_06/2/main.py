FILENAME = 'nginx_logs.txt'
result = []
n_dict = {}
with open (FILENAME, 'r') as file:
  temp_n = 1

  for line in file:
    
    temp_n = 1
    line_list = line.split()
    result.append((line_list[0],line_list[5][1:],line_list[6]))
    if line_list[0] in n_dict:
      n_dict[line_list[0]] = n_dict[line_list[0]] + 1
    else:
      n_dict[line_list[0]] = 1
  print([max(n_dict.items(), key=lambda k_v: k_v[1])])
    
  


#Если структура файла остается прежней, то подойдет и такой вариант 