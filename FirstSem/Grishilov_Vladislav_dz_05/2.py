def generator (n):
  temp_list=[]
  for i in range (0,n+1):
    if i%2 == 1:
      temp_list.append(i)
  return temp_list

print (generator(15))