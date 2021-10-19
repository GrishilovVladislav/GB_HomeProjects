l_1 = input().split()
for i_1 in range(0, len(l_1)):
  if l_1[i_1].isdigit():
    if len(l_1[i_1]) == 1:
      temp = l_1[i_1]
      l_1[i_1]='"0'+ temp + '"'
    else:
      temp = l_1[i_1]
      l_1[i_1]='"'+ temp + '"'
  elif (l_1[i_1].startswith('+') or l_1[i_1].startswith('-')) and l_1[i_1][1:].isdigit():
    if len(l_1[i_1]) == 2:
      temp_sign = l_1[i_1][0]
      temp = l_1[i_1][1:]
      l_1[i_1]='"'+ temp_sign +'0'+ temp + '"'
    else:
      temp = l_1[i_1]
      l_1[i_1]='"'+ temp + '"'
  else: 
    continue
s = ''
for i_1 in range(0, len(l_1)):  
  s+=l_1[i_1] + " "
print (s)