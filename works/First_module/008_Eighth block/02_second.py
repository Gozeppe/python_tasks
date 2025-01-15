#Задача 1. Матрица
#Напишите программу, которая выводит квадратную матрицу размера N на N. 
# В каждой нечётной строке матрицы идут числа от 1 до N, а в каждой чётной — просто числа, равные номеру этой строки.

N = int(input('Введите число: '))

for i in range(1, N + 1):  # Строки от 1 до N
    if i % 2 != 0:  # Нечетная строка
        for j in range(1, N + 1):  # Числа от 1 до N
            print(j, end=' ')
    else:  # Четная строка
        for j in range(1, N + 1):  # Все числа равны номеру строки
            print(i, end=' ')
    print()  # Переход на новую строку


#Задача 2. Чёрный ящик
#Преподаватель показал студентам несколько результатов программы и сказал: «Кто догадается, 
# что делает программа и как она это делает, получит зачёт автоматом». Студент Миша намерен получить этот зачёт.
#  Он заметил, что в результатах программы есть определённая закономерность. Вот некоторые результаты:

    n = int(input("Введите число: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j % 3 == 0:
            print(j, end='\t')
        else:
            print(i, end='\t')
    print()


#Задача 3. Координатные оси
#Напишите программу, которая рисует координатные оси на поле 20×50. Результат должен получиться таким:


#Что нужно поменять в коде, что в середине был не дефис, а вертикальная палочка?

x_lim = 50
y_lim = 20

for y in range(y_lim):
    for x in range(x_lim):
        if y == y_lim // 2:
            print('-', end='')
        elif x == x_lim // 2:
            print('|', end='')
        else:
            print(' ', end='')
    print()