FILENAME_1 = 'users.txt'
FILENAME_2 = 'hobby.txt'
FILENAME_3 = 'result.txt'

result_dict = {}
with open(FILENAME_3, 'w') as result:
  with open (FILENAME_1, 'r') as users:
    with open (FILENAME_2, 'r') as hobby:
      users_list = []
      hobby_list = []
      for line in users:
        temp_l = line.split(',')
        users_list.append((temp_l[0], temp_l[1], temp_l[2]))
      for line in hobby:
        hobby_list.append(line)
      for i in range(0, len(users_list)):
        if i < len(hobby_list):
          result_dict[users_list[i]] = hobby_list[i]
        else:
          result_dict[users_list[i]] = None
      result.write(str(result_dict))
