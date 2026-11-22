def lcm(a, b):
    x = 1
    while True:
        if b*x % a == 0: return b*x
        x+=1 

print(lcm(45, 70))
