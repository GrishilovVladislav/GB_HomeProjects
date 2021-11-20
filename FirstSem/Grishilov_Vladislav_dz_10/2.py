from abc import abstractmethod
class Clothes:
  def __init__(self, name = '', amount_of_cloth = 0):
    self.name = name

  @abstractmethod
  def count(self):
    return self.amount_of_cloth

class Coat(Clothes):
  def __init__(self, V, name = 'coat'):
    super().__init__(name)
    self.V = V
  @property
  def count(self):
    return self.V / 6.5 +0.5

class Costume(Clothes):
  def __init__(self, H, name = 'costume'):
    super().__init__()
    self.H = H
  
  def count(self):
    return self.H * 2 + 0.3

C1 = Coat (10)
Cs1 = Costume (5)

print(C1.count)
print(Cs1.count())