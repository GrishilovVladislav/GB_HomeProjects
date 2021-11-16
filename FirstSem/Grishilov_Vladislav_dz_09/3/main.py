class Worker:
  def __init__(self, name, surname, pos, wage, bonus):
    self.name = name
    self.surname = surname
    self.position = pos
    self._income = {
      "wage" : wage,
      "bonus" : bonus
    } 

class Position(Worker):
  def get_full_name(self):
    return self.name + ' ' + self.surname

  def get_full_income(self):
    return self._income["wage"] + self._income["bonus"]

P1 = Position('Ivan', 'Ivanov','Miner', 1000, 500)
print(P1.get_full_name())
print(P1.get_full_income())