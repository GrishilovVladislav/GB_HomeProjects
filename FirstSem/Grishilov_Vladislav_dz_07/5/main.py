from pathlib import Path
import os

def count (paths):

  if len(paths) == 0: 
    return
  for filename in paths:
    if Path(filename).is_file():
      d[0] = d[0] + 1
      if os.stat(filename).st_size < 100:   
        x1.append (filename[filename.find('.')+1:])  
        d[100] = (d[100] + 1, x1)
      if os.stat(filename).st_size < 1000 and os.stat(filename).st_size > 100:    
        x2.append (filename[filename.find('.')+1:])  
        d[1000] = (d[1000] + 1, x2)
      if os.stat(filename).st_size < 10000 and os.stat(filename).st_size > 1000:     
        x3.append (filename[filename.find('.')+1:])  
        d[10000] = (d[10000] + 1, x3)
      if os.stat(filename).st_size < 100000 and os.stat(filename).st_size > 10000:      
        x4.append (filename[filename.find('.')+1:])  
        d[100000] = (d[100000] + 1, x4)
    if Path(filename).is_dir() and filename[0] != '.' and filename not in ['__pycache__', '~']:   
      os.chdir(filename+ '/')  
      count(os.listdir())
      os.chdir('..')

d = {
       0 : 0,  
       100 : 0,
       1000 : 0,
       10000 : 0,
       100000 : 0
      }      
x1 = []
x2 = []
x3 = []
x4 = []

count (os.listdir())
print (d)