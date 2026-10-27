def plural(time, unit):
    return f'{time} {unit}' + ('s' if time > 1 else '')

def format_duration(seconds):
    if not seconds: return 'now'
    
    year = seconds // (86400*365)
    day = (seconds % (86400*365)) // 86400
    hour = (seconds % 86400) // 3600
    minute = (seconds % 3600) // 60
    second = seconds % 60

    units = [(year, 'year'), (day, 'day'), (hour, 'hour'), (minute, 'minute'), (second, 'second')]

    parts = [plural(t, u) for t, u in units if t]

    if len(parts) == 1:
        return parts[0]
    return ', '.join(parts[:-1]) + ' and ' + parts[-1]

print(format_duration(101956166))