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

def thesaurus_adv(names):
  names_dict = {}
  for i in range(0, len(names)):
      for k in range (0, len(names[i])):
        if names[i][k] == ' ':
          if names[i][k+1] in names_dict:
            temp_d = names_dict.pop(names[i][k+1])
            if names[i][0] in temp_d:
              temp_l = temp_d.pop(names[i][0])
              temp_l.append(names[i])
              temp_d[names[i][0]] = temp_l
            else:
              temp_d[names[i][0]] = names[i]
            names_dict[names[i][k+1]] = temp_d
            break
          else:
            names_dict[names[i][k+1]] = thesaurus([names[i]])
            break   
  return names_dict

print(thesaurus_adv(input('Enter your names comma separated: ').split(', '))) #Условие ввода: через запятую с пробелом 
                                                                              #Влад Гришилов, Юлиана Колешко, Юлиана Карпович, Геннадий Горин, Иван Иванов