from math import trunc
class Cell:
  def __init__(self, number):
    self.number = number
  def __add__(self, other):
    return Cell(self.number + other.number)
  def __sub__(self, other):
    if self.number > other.number:
      return Cell(self.number - other.number)
    else:
      raise Exception("result can't be negative")
  def __mul__(self, other):
    return Cell(self.number * other.number)
  def __truediv__(self, other):
    return Cell(trunc(self.number / other.number))
  def make_order(self, num):
    s = ''
    k = 1
    for i in range (0, self.number):
      s += '*'
      if k == num:
        s += '\n'
        k = 0
      k += 1
    return s
      
      
c1 = Cell(50)
c2 = Cell(100)
print ((c1+c2).make_order(50))