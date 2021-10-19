l_1 = input().split()
l_2 = []

for i_1 in range(0, len(l_1)):
  if l_1[i_1].isdigit():
    if len(l_1[i_1]) == 1:
      l_2.append('"0'+ l_1[i_1] +'"')
    else:
      l_2.append('"'+ l_1[i_1] +'"')
  elif l_1[i_1].startswith('+') or l_1[i_1].startswith('-') and l_1[i_1][1:].isdigit():
    if len(l_1[i_1]) == 2:
      l_2.append('"'+ l_1[i_1][0]+'0'+ l_1[i_1][1] +'"')
    else:
      l_2.append('"'+ l_1[i_1] +'"')
  else: 
    l_2.append(l_1[i_1])

s=""
for i_2 in range(0, len(l_2)):  
  s+=l_2[i_2] + " "
print (s)