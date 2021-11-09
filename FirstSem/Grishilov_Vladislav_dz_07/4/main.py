from pathlib import Path
import os

def count (paths):
  
  if len(paths) == 0: 
    return
  for filename in paths:
    if Path(filename).is_file():
      d[0] = d[0] + 1
      if os.stat(filename).st_size < 100:      
        d[100] = d[100] + 1
      if os.stat(filename).st_size < 1000 and os.stat(filename).st_size > 100:      
        d[100] = d[1000] + 1
      if os.stat(filename).st_size < 10000 and os.stat(filename).st_size > 1000:     
        d[100] = d[10000] + 1
      if os.stat(filename).st_size < 100000 and os.stat(filename).st_size > 10000:      
        d[100] = d[100000] + 1
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


count (os.listdir())
print (d)