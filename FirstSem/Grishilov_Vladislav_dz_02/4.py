l = input('Введите список сотрудников, разделяя их запятыми: ').split(',')
for i in range (0, len(l)):
  name =''
  for k in range (0, len(l[i])):
    if l[i][(len(l[i])-k-1)] == ' ':
      name = l[i][(len(l[i])-k-1):].title()
      break
  print ('Привет,' + name)   