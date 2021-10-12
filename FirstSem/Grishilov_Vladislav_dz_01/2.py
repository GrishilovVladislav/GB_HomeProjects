cube_list = [i**3 for i in range(0,1000) if i %2 == 1]
print (cube_list)

final_sum_1 = 0
final_sum_2 = 0
final_sum_3 = 0

n = 0
while n < len(cube_list):
  sum = 0
  temp = cube_list[n]
  while temp > 0:
    sum += temp % 10
    temp //=10
  if sum % 7 == 0:
    final_sum_1 += cube_list[n]
  n += 1
print ('==='*25)
print (final_sum_1)
print ('==='*25)

n = 0
temp_list = []
while n < len(cube_list):
  sum = 0
  temp_list.append(cube_list[n] + 17)
  temp = temp_list[n]  
  while temp > 0:
    sum += temp % 10
    temp //=10
  if sum % 7 == 0:
    final_sum_2 += temp_list[n]
  n += 1
print ('==='*25)
print (final_sum_2)
print ('==='*25)

n = 0
while n < len(cube_list):
  sum = 0
  temp = cube_list[n] + 17
  while temp > 0:
    sum += temp % 10
    temp //=10
  if sum % 7 == 0:
    final_sum_3 += cube_list[n] + 17
  n += 1
print ('==='*25)
print (final_sum_3)
print ('==='*25)