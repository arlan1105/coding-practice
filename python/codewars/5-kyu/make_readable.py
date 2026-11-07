def make_readable(seconds):
    hours = seconds // 3600
    minutes = seconds // 60 - (hours*60)
    seconds %= 60
    
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    
print(make_readable(86399))