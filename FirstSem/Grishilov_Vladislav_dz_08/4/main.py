def val_checker(func):
  def wrapper(*arg):
    for a in arg:
      if a < 0:
        raise ValueError(a, ' is wrong number (negative)')
        return
    func(*arg)
  return wrapper

@val_checker
def sum(*x):
  res = 0
  for n in x:
    res += n
  print (res)
  

sum(-10, 20, 30)
