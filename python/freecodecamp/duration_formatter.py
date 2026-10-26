def format(seconds):
    hour = seconds//3600
    minute = (seconds%3600)//60
    second = seconds%60

    if seconds < 3600: 
        return f'{minute}:{second:02d}'
    return f'{hour}:{minute:02d}:{second:02d}'
    
print(format(500))
print(format(1))
print(format(4000))
print(format(99999))