days = int(input('Enter N: '))
temperatures = [int(temp) for temp in input('Enter the temperatures: ').split()[:days]]
print('Warmer days:', sum(1 for day in range(1, days) if temperatures[day] > temperatures[day-1]))
