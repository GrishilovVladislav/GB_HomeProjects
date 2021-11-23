class Storage:
  storage = {}
  def __init__(self, obj):
    Storage.storage[obj.product_type] = obj.tech_dict
  def Show_Storage(self):
    print (Storage.storage)


class Technics:
  tech_dict = {}
  def __init__(self):
    self.product_type = 'Technics'
  def Add(self, obj, n):
    try:  
      if obj.type in Technics.tech_dict:
        Technics.tech_dict[obj.type] = Technics.tech_dict[obj.type] + n
      else:
        Technics.tech_dict[obj.type] = n
    except:
      print ('Invalid Input')
  def Del(self, obj, n):
    try:
      if obj.type in Technics.tech_dict:
        Technics.tech_dict[obj.type] = Technics.tech_dict[obj.type] - n
      else:
        print ('No Items')
    except:
      print ('Invalid Input')

class Monitor(Technics):
  def __init__(self):
    self.type = 'Monitor'
    

class Printer(Technics):
  def __init__(self):
    self.type = 'Printer'

class Scaner(Technics):
  def __init__(self):
    self.type = 'Scaner'

T1 = Technics()
S1 = Storage(T1)

T1.Add(Monitor(),10)
S1.Show_Storage()
T1.Add(Monitor(),10)
S1.Show_Storage()
T1.Add(Scaner(), 50)
S1.Show_Storage()
T1.Del(Scaner(), 10)
S1.Show_Storage()
T1.Add(Printer(), 100)
S1.Show_Storage()


T1.Add(Monitor(), '10')