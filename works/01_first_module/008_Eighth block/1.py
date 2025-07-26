levels = int(input("Введите количество уровней пирамиды: "))

current_odd_number = 1

for level in range(levels):
  print(' ' * (levels - level - 1) * 2, end='')
  for draw_num in range(level + 1):
    print(f"{current_odd_number:2}", end='  ')
    current_odd_number += 2
  print()
