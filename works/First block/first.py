#Программа для расчёта штрафа в Германии

import random

print('Система подсчёта штрафов')
print()

car_speed = random.randint(50, 150)
print(f'Скорость автомобиля: {car_speed} км/ч')
print()

fine_for_20_to_40 = 500

fine_for_40_to_60 = 1000

fine_for_60_to_80 = 2000

fine_for_80_and_over = 5000

country_speed = 90
town_speed = 60
is_Town = random_boolean = random.choice([True, False])
if is_Town == True:
  value = car_speed - town_speed
  if value < 20:
    print('Скорость в рамках допустимой в городе')
    print()
  elif value > 0:
    print(f'Скорость больше допустимой на {value} км/ч')
    print()
    print('В городе допустимая скорость равна 60 км/ч')
  print()
elif is_Town == False:
  value = car_speed - country_speed
  if value < 20:
    print('Скорость в рамках допустимой за городом')
    print()
  elif value > 0:
    print(f'Скорость больше допустимой на {value} км/ч')
    print()
    print('За городом допустимая скорость равна 90 км/ч')
    print()
  
#def fine_value(value):
#  if 20 <= value < 40:
#    return fine_for_20_to_40
#  elif 40 <= value < 60:
#    return fine_for_40_to_60
#  elif 60 <= value < 80:
#    return fine_for_60_to_80
#  elif value >= 80:
#    return fine_for_80_and_over
#  else:
#    return('Нет штрафа')
#print(f'Штраф: {fine_value(value)}')

if value < 20:
  print('Скорость не превышена или превышена незначительно')
elif value >= 20 and value < 40:
  print('Штраф - ' + str(fine_for_20_to_40))
elif value >= 40 and value < 60:
  print('Штраф - ' + str (fine_for_40_to_60))
elif value >= 60 and value < 80:
  print('Штраф - ' + str(fine_for_60_to_80))
elif value >= 80:
  print ('Штраф - ' +str(fine_for_80_and_over))


