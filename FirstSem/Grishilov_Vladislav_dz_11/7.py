class Complex_Number:
  def __init__(self, n, i):
    self.n = n
    self.i = i
    self.number = [n,i]
  def __add__(self, obj):
    return [self.n + obj.n, self.i + obj.i]
  def __mul__(self, obj):
    return [self.n * obj.n - self.i * obj.i, self.n * obj.i + self.i * obj.n]

C1 = Complex_Number(10, 5)
C2 = Complex_Number(5, 3)

print (C1 + C2)
print (C1 * C2)