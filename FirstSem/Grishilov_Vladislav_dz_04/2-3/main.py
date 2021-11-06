import requests
from datetime import datetime

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

def currency_rates(val):
  text = (requests.get(URL)).text
  val_date = datetime.strptime(text[text.find('Date')+6:text.find('name')-2], "%d.%m.%Y").date()
  text = text[text.find(val):]
  text = text[text.find('<Value>')+7:text.find('</Value>')]
  return text + ', ' + str (val_date)
print (currency_rates('USD'))