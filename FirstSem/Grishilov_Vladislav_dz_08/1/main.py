import re

def email_parse(email):
  try:
    res = re.split(r'@',email)
    dict_res = {
      'username': res[0],
      'domain' : res[1]
    }
  except:
    raise ValueError('wrong email adress')
    return
  return  dict_res

print (email_parse('vgrishilov@mail.ru'))
print (email_parse('vgrishilovmail.ru'))