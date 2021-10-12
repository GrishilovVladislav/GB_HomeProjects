ending_list = ['процент','процента','процентов']
digit = 0
while digit <= 100:
  if 10 < digit < 20:
    print (digit, ending_list[2]) 
  else:
    if digit % 10 == 1:
      print (digit, ending_list[0])   
    elif digit % 10 == 2 or digit % 10 == 3 or digit % 10 == 4:
      print (digit, ending_list[1]) 
    else:
      print (digit, ending_list[2])  
  digit += 1