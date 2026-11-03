def narcissistic(value):
    return sum(int(d)**len(str(value)) for d in str(value)) == value
    
print(narcissistic(1634))