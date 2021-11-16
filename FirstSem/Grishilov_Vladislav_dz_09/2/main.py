class Road:
  def __init__(self, length, width):
    self._length = length
    self._width = width

  def count(self, mass, thickness):
    return mass*thickness*self._length*self._width
    

R = Road(1000, 30);
print(R.count(25, 5))