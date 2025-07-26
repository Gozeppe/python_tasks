row_count = int(input('Введите количество рядов: '))
seats_count = int(input('Введите количество сидений: '))
meter_between = int(input('Введите количество свободных метров между рядами: '))

for seats in range (row_count):
  print('=' * seats_count, '*' * meter_between, '=' * seats_count)