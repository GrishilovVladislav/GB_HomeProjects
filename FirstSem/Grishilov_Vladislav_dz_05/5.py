def func (l):
  result = []
  for i in range (0, len(l)):
    if l[i] in result:
      continue
    else:
      result.append(l[i])
  return result

##############################################################

def generator(l):
  temp = []
  for i in range (0, len(l)):
    if l[i] in temp:
      continue
    else:
      yield l[i]
      temp.append(l[i])

############################################################## 

scr = (input('Enter your list: ').split())                     
scr = [int(x) for x in scr]
print (func(scr))
print (list(generator((scr))))
# Со множеством не получается так сделать, тк значения там сортируются в определенном порядке или рандомно перемешиваются