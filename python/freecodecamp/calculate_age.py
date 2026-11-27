from datetime import datetime

def calculate_age(birthday):
    now = datetime(2025, 11, 27)
    formatted = datetime.strptime(birthday, '%Y-%m-%d')
    return now.year - formatted.year - ((formatted.month, formatted.day) > (now.month, now.day))

print(calculate_age("2000-11-28"))
