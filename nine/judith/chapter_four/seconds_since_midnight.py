def second_since_midnight(hour, minute, second):
    hour_in_seconds = 3600
    minute_in_seconds = 60
    return (hour_in_seconds * hour) + (minute_in_seconds * minute) + second


print(second_since_midnight(15, 45, 30))
