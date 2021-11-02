def generator (l):
  for i in range (1, len(l)):
    if l[i-1] < l[i]:
      yield l[i]
  
l = (input('Enter your list: ').split())
l = [int(x) for x in l]
print (list(generator(l)))