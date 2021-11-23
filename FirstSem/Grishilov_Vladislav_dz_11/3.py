class List_Maker:
  L = []
  def __init__(self):
    while (True):
      s = input()
      if s == 'stop':
        break
      try:
        s = int(s)
        self.L.append(s)
      except:
        print('This is not an int definition')
    print (self.L)
    
L1 = List_Maker()
