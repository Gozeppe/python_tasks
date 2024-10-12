# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n = int(input('Введите число: '))

for rows in range (n + 1):
    for col in range (n + 1):
        pyramid = rows * col
        print(pyramid)
    print()