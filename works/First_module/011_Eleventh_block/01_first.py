# ; Задача 1. Сумма чисел 2
# ; Пользователь вводит число N. Напишите функцию summa_n, которая принимает одно целое положительное число N 
# и находит сумму всех чисел от 1 до N включительно. Функция вызывается два раза: сначала от числа N, а затем от полученной суммы.

# ; Пример работы программы:

# ; Введите число: 5
# ; Сумма от 1 до 5 = 15
# ; Сумма от 1 до 15 = 120

def suma_n(N):
    return sum(range(1, N + 1))

N = int(input('Введите число: '))

first_num = suma_n(N)
second_num = suma_n(first_num)
print(f'От 1 до {N} сумма равна {first_num}')
print(f'От 1 до {first_num} сумма равна {second_num}')

# ; Задача 2. «Назад в будущее»
# ; Вы — один из разработчиков языка программирования Python, и вы пишете специальный математический модуль,
#  который можно было бы просто подключить внутри программы и облегчить жизнь всем программистам.

# ; Реализуйте функцию gcd, которая получает два параметра — два числа — и возвращает наибольший общий делитель этих двух чисел.

# ; Пример работы программы:

# ; Введите первое число: 6
# ; Введите второе число: 10
# ; НОД = 2

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Пример работы программы
if __name__ == "__main__":
    # Вводим числа
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    # Вычисляем НОД
    result = gcd(a, b)

    # Вывод результата
    print(f"НОД = {result}")


# ; Задача 3. Приоритет задач
# ; В одном дата-центре ресурсы распределены так, что сначала обрабатываются крупные задачи, а затем уже идут небольшие.
#  Каждая из этих задач, по сути, просто огромный поток цифр. Ваша задача, как программиста этого центра, 
# написать программу, которая поможет определять, какую из задач нужно решать в первую очередь. 

# ; Вводится последовательность из N чисел. Нужно определить номер числа, у которого больше всего цифр, 
# и вывести на экран соответствующее сообщение. Если число отрицательное, то считать его за 0. 
# Для подсчёта количества цифр реализуйте функцию numeral_count.

# ; Пример работы программы:

# ; Введите кол-во задач: 4
# ; Введите число: 6
# ; Введите число: 14
# ; Введите число: 1
# ; Введите число: 13434

# ; Первая задача на обработку: 13434

def numeral_count(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def numeral_check(n):
    max_count = 0
    max_number = 0
    for _ in range(1, n + 1):

        new_value = int(input("Введите число: "))
        if new_value < 0:
            new_value = 0

        cipher_count = numeral_count(new_value)
        if cipher_count > max_count:
            max_count = cipher_count
            max_number = new_value

    return max_number


how_many = int(input("Введите количество чисел: "))
print("Первая задача на обработку: ", numeral_check(how_many))