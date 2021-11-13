def type_logger(func):
  def wrapper(*arg):
    for a in arg:
      print(a, ' : ', type(a))
    func(*arg)
  return wrapper

@type_logger  
def calc_cube(x):
  print (x*x*x)
  
@type_logger  
def print_name(name, s_name):
  print(name, ' ', s_name)  

calc_cube(10)
print_name ('Ivan', 'Ivanov')