def rgb(r, g, b):
    a = [max(0, min(255, x)) for x in [r, g, b]]
    return f'{a[0]:02X}{a[1]:02X}{a[2]:02X}' 
  
print(rgb(-20, 275, 125))