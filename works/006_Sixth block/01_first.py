#Задача 1. Таблица кубов
#Паше для проекта по математике нужна таблица кубов (третья степень числа) только чётных чисел от 1 до N. 
#Напишите программу, которая выведет ему эту таблицу на экран.
#Не используйте условные операторы, выведите формулу, как мы сделали это в уроке.

N = int(input('Введите число: '))

for i in range(2, N + 1, 2):
    cube = i ** 3  # Куб чётного числа
    print(f'{i}^3 = {cube}')

#Задача 2. Деление клетки
#Реализуйте программу, разобранную в уроке.

#В одной лаборатории наблюдают за одноклеточной амёбой. 
#Мы знаем, что каждые три часа она делится на 2 клетки. 
#Нам нужно для этой лаборатории написать программу, которая будет выводить сколько прошло часов и сколько получилось клеток. 
#Также нас попросили писать на каждом этапе деления сколько осталось часов до завершения наблюдения, 
# чтобы ученым было проще формулировать выводы на определённом этапе наблюдения.

total_hours = int(input("Количество часов: "))
cell_count = 1
for hour in range(1, total_hours // 3 + 1):
    cell_count *= 2
    print("Прошло часов:", hour * 3)
    print("Количество клеток:", cell_count)
    print("Осталось часов:", total_hours - hour * 3)
print("Наблюдение завершено!")

# Задача 3. Квадраты нечётных чисел
# Вводится число N. Напишите программу, которая выводит квадраты нечетных чисел от 1 до N.
# Нельзя использовать условные операторы. Можно использовать цикл while, но постарайтесь всё-таки решить с помощью конструкции for in range.
# Не нужно искать решение в интернете, попробуйте подумать сами, в следующем видео мы обязательно разберём эту задачу.

n = int(input("До какого числа выводить квадраты: "))
for i in range(1, n // 2 + n % 2 + 1):
    odd_number = i * 2 - 1
    print("Число:", odd_number, "Квадрат числа:", odd_number ** 2)