def generator (l1, l2):
  res = ()
  for i in range (0,len(l1)):
    if i < len(l2):
      res = (l1[i], l2[i])
      yield res
    else:
      res = (l1[i], None)
      yield res
  

l1 = input('Enter the first list: ').split()   #Иван Ананстасия Геннадий Антон Евгений Юлия Анна
l2 = input('Enter the second list: ').split()  #9А 10Б 7В 11Г
print (list(generator(l1, l2)))