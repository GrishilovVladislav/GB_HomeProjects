def thesaurus(names):
  names_dict = {}
  for i in range(0, len(names)):
    if names[i][0] in names_dict:
      temp_l = names_dict.pop(names[i][0])
      temp_l.append(names[i])
      names_dict[names[i][0]] = temp_l
      
    else: 
      names_dict[names[i][0]] = [names[i]]
  return names_dict

print(thesaurus(input('Enter your names: ').split()))