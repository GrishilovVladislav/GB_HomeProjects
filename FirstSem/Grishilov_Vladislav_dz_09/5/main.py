class Stationery:
  def __init__(self,title = None):
    self.title = title

  def draw(self):
    print ('Stationery class')

class Pen (Stationery):
  def __init__(self,title = 'Pen'):
    self.title = title

  def draw(self):
    print ('Pen class')

class Pencil (Stationery):
  def __init__(self,title = 'Pencil'):
    self.title = title

  def draw(self):
    print ('Pencil class')


class Handle (Stationery):
  def __init__(self,title = 'Handle'):
    self.title = title

  def draw(self):
    print ('Handle class')

P1 = Pen()
P1.draw()

P2 = Pencil()
P2.draw()

H1 = Handle()
H1.draw()