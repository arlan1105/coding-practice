from datetime import datetime

def moon_phase(date_string):
    ref = datetime(2000, 1, 6)
    year, month, day = map(int, date_string.split('-')) 
    date = datetime(year, month, day) 
 
    cycle_day = (date - ref).days % 28
    
    if cycle_day < 7: return 'New'
    elif cycle_day < 14: return 'Waxing'
    elif cycle_day < 21: return 'Full'
    return 'Waning'

print(moon_phase("2014-10-15"))

# from datetime import date
# def moon_phase(date_string):
#     ref = date(2000, 1, 6)
#     d = date.fromisoformat(date_string)
#     cycle_day = (d - ref).days % 28