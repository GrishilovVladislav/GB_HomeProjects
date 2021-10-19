l = input('Введите цены через пробел: ').split()
l.sort(key = lambda k: float(k.split()[0]))
for i in range (0, len(l)):
  l[i] = float(l[i])
  rub = str(int(l[i]//1))
  kop = str(int((l[i]*100)%100))
  if i+1 == len(l):
    if (len(kop) == 1):
      print (rub, 'руб','0' + kop, 'коп.')
    else:
      print (rub, 'руб', kop, 'коп.')
  else:
    if (len(kop) == 1):
      print (rub, 'руб','0' + kop, 'коп, ', end='')
    else:
      print (rub, 'руб', kop, 'коп, ', end='')
    
print('')
print('='*50)
print('')

l_new = l
l_new.reverse()
for i in range (0, len(l_new)):
  rub = str(int(l_new[i]//1))
  kop = str(int((l_new[i]*100)%100))
  if i+1 == len(l_new):
    if (len(kop) == 1):
      print (rub, 'руб','0' + kop, 'коп.')
    else:
      print (rub, 'руб', kop, 'коп.')
  else:
    if (len(kop) == 1):
      print (rub, 'руб','0' + kop, 'коп, ', end='')
    else:
      print (rub, 'руб', kop, 'коп, ', end='')

print('')
print('='*50)
print('')

print('5 смаых дорогих: ', end='')
for i in range (0, 5):
  rub = str(int(l[i]//1))
  kop = str(int((l[i]*100)%100))
  if i == 4:
    if (len(kop) == 1):
      print (rub, 'руб','0' + kop, 'коп.')
    else:
      print (rub, 'руб', kop, 'коп.')
  else:
    if (len(kop) == 1):
      print (rub, 'руб','0' + kop, 'коп, ', end='')
    else:
      print (rub, 'руб', kop, 'коп, ', end='')