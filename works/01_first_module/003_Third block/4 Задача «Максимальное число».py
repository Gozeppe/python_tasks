#Задача «Максимальное число»
#Пользователь вводит три числа.

#Напишите программу, которая выводит на экран максимальное из этих трёх чисел (все числа разные). Используйте дополнительные переменные, если нужно.

#Перейдите в сервис Replit и попробуйте решить задачу самостоятельно. Чтобы увидеть подсказку, нажмите на кнопку ниже

first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third number: '))

if first_num > second_num:
  bigger_of_first_two = first_num
else:
  bigger_of_first_two = second_num

if bigger_of_first_two > third_num:
  print('Biggest number is ', bigger_of_first_two)
else:
  print('Biggest number is ', third_num)