next_day = {
    'Sunday': 'Monday', 
    'Monday': 'Tuesday', 
    'Tuesday': 'Wednesday', 
    'Wednesday': 'Thursday', 
    'Thursday': 'Friday', 
    'Friday': 'Saturday', 
    'Saturday': 'Sunday',
    None: None
}

next_period = {
    'AM': 'PM',
    'PM': 'AM'
}

def add_info(count):
    """This function gives additional information on the result of the add_time function."""
  if count == 0:
    message = ''
  elif count == 1:
    message = " (next day)"
  else:
    message = f" ({count} days later)"
  return message

def check_time_transition(old_hour, new_hour, period, day, count):
  if old_hour <= 11 and new_hour == 12: 
    # definitely change AM to PM or vice versa
    old_period = period
    new_period = next_period[period]
    if old_period == 'PM' and new_period == 'AM':
      new_day = next_day[day]
      count += 1
    else:
      new_day = day
    return new_period, new_day, count
  else:
    return period, day, count

def add_time(start, duration, day=None):
  """
  add_time function takes in two required parameters and one optional parameter: 
  - a start time in the 12-hour clock format (ending in AM or PM), 
  - a duration time that indicates the number of hours and minutes, 
  - (optional) a starting day of the week, case insensitive. 
  
  The function should add the duration time to the start time and return the result.

  Example:
  add_time("11:43 PM", "24:20", "tueSday")
  # Returns: 12:03 AM, Thursday (2 days later)
  """
  period = start[-2:]
  hour, minute = [int(t) for t in start[:-3].split(':')]
  dhour, dminute = [int(d) for d in duration.split(':')]
  count = 0
  if day != None: day = day.lower().capitalize()

  while dminute > 0:
    minute_left = 60 - minute
    if dminute < minute_left:
      minute += dminute
      dminute -= dminute
    else: # dminute > minute_left
      hour_before = hour
      hour += 1
      minute = 0
      dminute -= minute_left
      period, day, count = check_time_transition(hour_before, hour, period, day, count)

  while dhour > 0:
    hour_left = 12 - hour
    if hour_left == 0:
      if dhour < 12:
        hour = dhour
        dhour -= dhour
      else: # dhour >= 12
        hour = 12
        dhour -= 12
        
        old_period = period
        period = next_period[period]
        if old_period == 'PM' and period == 'AM':
          day = next_day[day]
          count += 1
          
    else: 
      if dhour < hour_left:
        hour_before = hour
        hour += dhour
        dhour -= dhour
        period, day, count = check_time_transition(hour_before, hour, period, day, count)
        
      else: # dhour >= hour_left
        hour_before = hour
        hour += hour_left
        dhour -= hour_left
        period, day, count = check_time_transition(hour_before, hour, period, day, count)
        
  
  minute = '0'+str(minute) if len(str(minute)) == 1 else str(minute)
  result = f"{hour}:{minute} {period}"
  if day: result += f", {day}"
  result += f"{add_info(count)}"

  return result