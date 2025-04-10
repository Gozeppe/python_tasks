# 🧨 Задание 1: Арифметика
# Создай две переменные x = 7 и y = 3, а затем выведи:

# их сумму

# разность

# произведение

# результат деления

# остаток от деления

# результат целочисленного деления

# возведение в степень

x = 7
y = 3

summ = x + y
difference = x - y  
multiply = x * y
divide = x / y
remainder = x % y  
floor_divide = x // y  
power = x ** y  

# 🧨 Задание 2: Логические операторы
# Создай две переменные a = True, b = False. Выведи:

# a and b

# a or b

# not a

a = True
b = False

print(f'{a} and {b} = {a and b}')
print(f'{a} or {b} = {a or b}')
print(f'not {a} = {not a}')

# 🧨 Задание 3: Сравнение
# Пусть пользователь вводит два числа. Сравни их:

# больше ли первое второго

# равно ли

# меньше ли

# не равно ли

# Выводи результаты в виде:

# Первое число больше второго: True/False

first_digit = int(input('Введите первое число: '))
second_digit = int(input('Введите второе число: '))

print("Первое число больше второго:", first_digit > second_digit)
print("Первое число равно второму:", first_digit == second_digit)
print("Первое число меньше второго:", first_digit < second_digit)
print("Числа не равны:", first_digit != second_digit)

# 🧨 Задание 4: Сложные выражения
# Создай переменную num = 10. Выведи результат следующих выражений:

# (num + 5) * 2

# num ** 2 - 10

# num % 3 + num // 2

num = 10

print((num + 5) * 2)
print(num ** 2 - 10)
print(num % 3 + num // 2)