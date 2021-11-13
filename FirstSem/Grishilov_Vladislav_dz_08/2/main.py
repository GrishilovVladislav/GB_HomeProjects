import re

FILENAME = 'nginx_logs.txt'

IP_PATTERN = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}')
DATE_PATTERN = re.compile('\[.{1,}\]')
INFO1_PATTERN = re.compile('"\S{1,} ')
INFO2_PATTERN = re.compile('/\S{1,}/product\S{1,} ')
INFO3_PATTERN = re.compile('\d{1,} \d{1,} ')


def str_parse(line):
  ip = IP_PATTERN.search(line).group()
  dt = DATE_PATTERN.search(line).group()[1:-1]
  i1 = INFO1_PATTERN.search(line).group()[1:-1]
  i2 = INFO2_PATTERN.search(line).group()[:-1]
  i3 = INFO3_PATTERN.search(line).group()[:-1].split()

  res = (ip, dt, i1, i2, i3[0], i3[1])
  return  res

with open (FILENAME, 'r') as file:
  for line in file:
    print(str_parse(line))