def too_much_screen_time(hours):
    for day_hours in hours:
        if day_hours >= 10:
            return True
          
    for i in range(len(hours) - 2):
        three_day_avg = (hours[i] + hours[i+1] + hours[i+2]) / 3
        if three_day_avg >= 8:
            return True
   
    weekly_avg = sum(hours) / 7
    if weekly_avg >= 6:
        return True
    
    return False
