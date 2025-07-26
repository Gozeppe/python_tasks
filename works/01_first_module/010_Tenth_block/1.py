def reverse_number_recursive(number, reversed_number=0):
  if number == 0:
    return reversed_number
  return reverse_number_recursive(number // 10, reversed_number * 10 + number % 10)


while True:
  value = int(input('Введите число (0 для выхода): '))

  if value == 0:
    print('Программа завершена!')
    break

  reversed_number = reverse_number_recursive(value)
  print(f'Число наоборот: {reversed_number}')
