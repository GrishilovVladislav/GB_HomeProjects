def generator (n):
  for i in range (0,n+1):
    if i%2 == 1:
      yield i

print (list(generator(15)))