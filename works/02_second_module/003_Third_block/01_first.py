# Задача 1. Кубы и квадраты
# Пользователь вводит числа A и B. Напишите программу, которая генерирует два списка: в первом лежат кубы чисел в диапазоне от А до В, 
# во втором — квадраты чисел в этом же диапазоне. Выведите списки на экран. 
# Для генерации используйте list comprehensions (как и в следующих задачах).

# Пример:
# Левая граница: 5
# Правая граница: 10
# Список кубов чисел в диапазоне от 5 до 10: [125, 216, 343, 512, 729, 1000]
# Список квадратов чисел в диапазоне от 5 до 10: [25, 36, 49, 64, 81, 100]

user_number_A = int(input('Enter number A: '))
user_number_B = int(input('Enter number B: '))

kvad = [x**2 for x in range(user_number_A, user_number_B + 1)]
qube = [x**3 for x in range(user_number_A, user_number_B + 1)]

print(f'Kvad list: {kvad}')
print(f'Qube list: {qube}')

# Задача 2. Сообщение
# Илья решил безобидно подшутить над другом и написал программу для смартфона,
#  которая при отправке сообщения удваивает каждый символ строки и заодно к каждому удвоенному добавляет ещё один дополнительный.

# Пользователь вводит строку и дополнительный символ. Напишите программу, которая генерирует два списка: 
# в первом списке каждый элемент — удвоенная буква первой строки,
#  во втором списке каждый элемент — конкатенация элемента первого списка и дополнительного символа.

 

# Пример:

# Введите строку: привет

# Введите дополнительный символ: !

 

# Список удвоенных символов: ['пп', 'рр', 'ии', 'вв', 'ее', 'тт']

# Склейка с дополнительным символом: ['пп!', 'рр!', 'ии!', 'вв!', 'ее!', 'тт!']

specials = ('!', '?')

first = input('Enter First String: ')
second = input('Enter Second String: ')

count1 = sum(1 for ch in first if ch in specials)
count2 = sum(1 for ch in second if ch in specials)

if count1 > count2:
    result = first + ' ' + second
elif count2 > count1:
    result = second + ' ' + first
else:
    result = 'Ой'

print(f'Third Message: {result}')

# Задача 3. Повышение цен
# Дан список цен на пять товаров с точностью до копейки. Так как экономика даёт о себе знать, мы спрогнозировали, 
# что через год придётся повышать цены на X процентов, а ещё через один год — ещё на Y процентов.

# Напишите программу, которая получает на вход список цен на товары 
# (вещественные числа, список генерируется также с помощью list comprehensions) и выводит в одну строку общую сумму стоимости товаров за каждый год.

prices = [float(input(f"Enter price {i+1}: ")) for i in range(5)]

first_increase = float(input('How much increase for the first year: '))
second_increase = float(input('How much increase for the second year: '))

total_sum = sum(prices)

first_sum_increase = [price * (1 + first_increase / 100) for price in prices]
first_total = sum(first_sum_increase)

second_sum_increase = [price * (1 + second_increase / 100) for price in first_sum_increase]
second_total = sum(second_sum_increase)

third_total = [total_sum, first_total, second_total]
print(third_total)


# Пример:

# Цена на товар: 1.09

# Цена на товар: 23.56

# Цена на товар: 57.84

# Цена на товар: 4.56

# Цена на товар: 6.78

# Повышение на первый год: 0

# Повышение на второй год: 10

# Сумма цен за каждый год: 93.83 93.83 103.21

