def get_weekday(date_string):
    weekdays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    yr, mo, day = map(int, date_string.split('-'))

    if mo < 3:
        mo+=12
        yr-=1

    J, K = divmod(yr, 100)

    zeller = (day + ((13*(mo+1))//5) + K + (K//4) + (J//4) + (5*J)) % 7

    return weekdays[zeller]

print(get_weekday("2025-11-06"))
