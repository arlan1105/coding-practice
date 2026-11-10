num = int(input('Enter number: '))
if num%10> 4: print('Rounded:', num + (10 - num%10))
else: print('Rounded:', num - (num%10))
