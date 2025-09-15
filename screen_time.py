def too_much_screen_time(hours):
    for hours_per_day in hours:
        if hours_per_day >= 10:
            return True
    for i in range(5):
        three_days = hours[i:i+3]
        avg = sum(three_days)/3
        if avg >= 8:
            return True
    week_average = sum(hours)/7
    if week_average >= 7:
        return True

    return False
