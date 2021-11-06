import requests
from datetime import datetime
from sys import argv

l = argv[1:]
URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

def currency_rates(list_val):
  for val in list_val:
    text = (requests.get(URL)).text
    val_date = datetime.strptime(text[text.find('Date')+6:text.find('name')-2], "%d.%m.%Y").date()
    text = text[text.find(val):]
    text = text[text.find('<Value>')+7:text.find('</Value>')]
    yield text + ', ' + str (val_date)

for i in list(currency_rates(l)):
  print (str(i))