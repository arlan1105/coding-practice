meter3 = int(input('Enter cubic meters used: '))
print('Bill:', sum(15 if n < 10 else 25 for n in range(meter3)))
