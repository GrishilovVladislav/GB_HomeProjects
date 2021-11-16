class Car:
  def __init__(self, speed = None, color = None, name = None, is_police = False):
    self.speed = speed
    self.color = color
    self.name = name
    self.is_police = is_police
  def go(self):
    print ('Car is riding')
  def stop(self):
     print ('Car has stopped')
  def turn(self, direction):
    print ('Car has turned ', direction)
  def show_speed(self):
    print (self.speed)  

class TownCar(Car):
  def show_speed(self):
    if self.speed > 60:
      print (f'Over speed! {self.speed} > 60')
    else:
      print (self.speed)
  
class WorkCar(Car):
  def show_speed(self):
    if self.speed > 40:
      print (f'Over speed! {self.speed} > 40')
    else:
      print (self.speed)

class PoliceCar(Car):
  def __init__(self, speed = None, color = None, name = None, is_police = True):
    Car.__init__(self, speed , color , name )
    self.is_police = True
    

P1 = PoliceCar(100, 'red', 'BMW')
P1.show_speed()
print(P1.is_police)

T1 = TownCar(70, 'blue', 'BMW')
T1.show_speed()

W1 = WorkCar(30, 'black', 'Mercedes')
W1.show_speed()