ending_list = ['процент','процента','процентов']
while True:
  digit = int(input('Введите число '))
  if 10 < digit < 20:
    print (digit, ending_list[2]) 
  else:
    if digit % 10 == 1:
      print (digit, ending_list[0])   
    elif digit % 10 == 2 or digit % 10 == 3 or digit % 10 == 4:
      print (digit, ending_list[1]) 
    else:
      print (digit, ending_list[2])  