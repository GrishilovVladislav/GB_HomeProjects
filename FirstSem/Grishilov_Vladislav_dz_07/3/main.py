from pathlib import Path

FILENAME = 'config.txt'
MAINDIRECT = ''

def make_dir(lines, path = 'my_project', i = 1, k = 0):
  temp_k = lines[i].find('-')
  if temp_k - k > 0:
    path = path + r'/' + lines[i][temp_k+1:]
    if i == len(lines)-1:
      p = Path(path)
      p.mkdir(parents = True, exist_ok = True)
      return
    else:
      make_dir (lines, path, i + 1, k + 2)
  elif k >= 2:
    p = Path(path)
    path = path[:path.rfind(r'/')]
    p.mkdir(parents = True, exist_ok = True)
    make_dir (lines, path, i , k - 2)
  return

  

with open (FILENAME, 'r') as file:
  lines = []
  for line in file:
    lines.append(line[0:line.find('|--')] + line[line.find('|--')+2:-1])
print (lines)

make_dir(lines)


