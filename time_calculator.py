def add_time(start, duration, day = False):
  daylist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  
  minutes = int(start.split()[0].split(":")[1]) + int(duration.split(":")[1])
  hours = int(start.split()[0].split(":")[0]) + int(duration.split(":")[0])
  ampm = start.split()[1]
  days = 0
  
  newday = ''
  if day != False:
    newday = day.title()

  if ampm == 'PM':
    hours += 12
    ampm = 'AM'

  if minutes//60 >= 1:
    hours += minutes//60
    minutes -= (minutes//60) * 60
  
  
  if(minutes < 10):
    minutes = '0' + str(minutes)
  
  if hours//24 >= 1:
    days = hours//24
    hours -= (hours//24) * 24

  if hours == 0:
    hours = 12
  elif hours == 12:
    ampm = 'PM'
  elif hours > 12:
    hours -= 12
    ampm = 'PM'
  else:
    ampm = 'AM'

  if day is False:
    if days == 0:
      return '{}:{} {}'.format(hours, minutes, ampm)
    elif days == 1:
      return '{}:{} {} (next day)'.format(hours, minutes, ampm)
    else:
      return '{}:{} {} ({} days later)'.format(hours, minutes, ampm, days)
  else:
    if days == 0:
      return '{}:{} {}, {}'.format(hours, minutes, ampm, newday)
    elif days == 1:
      return '{}:{} {}, {} (next day)'.format(hours,minutes,ampm,daylist[daylist.index(newday)+1])
    else:
      return '{}:{} {}, {} ({} days later)'.format(hours,minutes,ampm,daylist[daylist.index(newday)+days], days)
  
      

  
    
    
