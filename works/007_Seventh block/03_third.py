#Задача 1. Доска
#Используя новые знания о циклах и операторе end, напишите программу, которая выводит на экрану вот такую «доску»:

print("-" * 10)  # Верхняя граница доски

for i in range(8):  # Для строк между границами
    print("|", end="")  # Левая граница
    print("0" * 8, end="")  # Внутри доски
    print("|")  # Правая граница

print("-" * 10)  # Нижняя граница доски

#Задача 2. Локальная сеть
#У Никиты дома есть много компьютеров, которые он хочет подключить к одной локальной сети. 
# Для этого ему нужно сгенерировать айпи адрес для каждого компьютера. Айпи адрес записывается как 4 числа, которые отделяются точкой.
#  Не долго думая, для генерации Никита решил использовать арифметическую прогрессию, причём первые 3 числа в адресе - это члены прогрессии, 
# а последнее число - это её сумма.

#Напишите программу, где пользователь вводит:

#Первый член прогрессии.
#Разность (шаг, с которым будут увеличиваться числа).
#И в результате получает IP-адрес.

IP_number = int(input('Введите число: '))
IP_step = int(input('Введите число: '))
sum = 0

for step in range(3):
     print(f'{IP_number}', end=".")
     sum += IP_number
     IP_number += IP_step
print(f"{sum}")



#Задача 3. Табло
#Петя пишет компьютерную спортивную игру, где каждый “гол” это десять очков. Он хочет сделать красивое табло с градацией этих очков.

#Пользователь вводит число N (N >= 0). Реализуйте программу, которая выводит в одну строчку каждое десятое число, разделяя их символами “-=-”. 
# Эти же символы стоят перед первым числом и после последнего.

#Пример:

#Введите число: 50

#-=- 0 -=- 10 -=- 20 -=- 30 -=- 40 -=- 50 -=-


N = int(input('Введите число: '))

print('-=-', end='')
for symbol in range(0, N + 1, 10):
    print(f'{symbol}', end=' -=- ')