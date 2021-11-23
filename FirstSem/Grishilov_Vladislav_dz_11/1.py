MOUNTH31 = [1,3,5,7,8,10,12]
str_date = ''
class Date_Class:
  str_date = ''
  def __init__(self, str_date):
    Date_Class.str_date = str_date

  @classmethod
  def Transform(cls):
    cls.numbers = cls.str_date.split('-')
    for i in range (0, len(cls.numbers)):
      cls.numbers[i] = int(cls.numbers[i])
    return cls.numbers

  @staticmethod
  def Validate(self):
    if self.numbers[1] in MOUNTH31:
      if self.numbers[0] in range (1,32):
        return 
      else:
        raise ValueError('Incorrect data input')
    elif self.numbers[1] == 2:
      if self.numbers[0] in range (1,30):
        return
      else:
        raise ValueError('Incorrect data input')
    elif self.numbers[1] >= 1 and self.numbers[1] <= 12:
      if self.numbers[0] in range (1,31):
        return
      else:
        raise ValueError('Incorrect data input')
    else:
      raise ValueError('Incorrect data input')

D1 = Date_Class('31-15-2003')
print(Date_Class.Transform())
Date_Class.Validate(D1)