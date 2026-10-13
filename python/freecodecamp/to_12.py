def to_12(time):

    hour, minute = time[0:2], time[2:5]
    meridiem = 'PM' if int(hour) >= 12 else 'AM'

    return f'{int(hour)% 12 or 12}:{minute} {meridiem}'

print(to_12("0030"))