class Matrix:
  def __init__(self, l):
    self.l = l

  def __str__(self):
    s = ''
    for el_1 in self.l:
      s+='| '
      for el_2 in el_1:
        s = s + str(el_2) + ' '
      s+='|\n'
    return s

  def __add__(self, other):
    if len(self.l) == len(other.l):
      for k in range(0, len(self.l)):
        if len(self.l[k]) == len(other.l[k]):
          for i in range(0,len(self.l[k])):
            self.l[k][i]+=other.l[k][i]
        else:
          raise ValueError('matrices must be the same size')
    else:
      raise ValueError('matrices must be the same size')
    return Matrix(self.l)


m1 = [[1,2,3,4],[3,4,5,6]]
m2 = [[3,8,-3,2],[5,-10,1,2]]

Mat1 = Matrix(m1)
Mat2 = Matrix(m2)
print (Mat1)
MatRes = Mat1 + Mat2
print (MatRes)