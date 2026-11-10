first = int(input('Enter seats in first row: '))
rows = int(input('Enter number of rows: '))
print('Total seats:', sum(first+(seats*2) for seats in range(rows)))
