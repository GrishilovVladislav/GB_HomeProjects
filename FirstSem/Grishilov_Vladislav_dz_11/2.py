class Zero_Div(Exception):
  def __init__(self, txt):
    self.txt = txt

try:
  print (int(input())/int(input()))
except ZeroDivisionError:
  raise Zero_Div('Division by zero impossible')

