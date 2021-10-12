while True:
  duration = int(input ('Enter the duration in seconds: '))
  dur_days = duration // (24*60*60)
  dur_hours = duration // (60*60)
  dur_minutes = duration // 60

  if dur_days > 0:   
    print (dur_days, 'days', dur_hours - dur_days*24, 'h',dur_minutes - dur_hours*60, 'min', duration%60, 'sec')
  else:
    if dur_hours > 0:
      print (dur_hours - dur_days*24, 'h', dur_minutes - dur_hours*60, 'min', duration%60, 'sec')
    else:
      if dur_minutes > 0:
        print (dur_minutes - dur_hours*60, 'min', duration%60, 'sec')
      else: 
        print (duration, 'sec')