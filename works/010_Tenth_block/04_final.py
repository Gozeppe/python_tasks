print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N 
# и выводит сумму всех чисел от 1 до N включительно.
# 
# Пример работы программы:
# Введите число: 5
# 
# Я знаю, что сумма чисел от 1 до 5 равна 15

def calculate_and_output_sum_numbers(numbers):
    summ = 0
    for number in range(1, numbers+1):
      summ += number
    print("Я знаю, что сумма чисел от 1 до", numbers, "равна", summ)

numeric = int(input("Введите число "))
calculate_and_output_sum_numbers(numeric)


print('Задача 2. Функция в функции')

# Евгений проходит специальный тест по программированию.
# У него всё шло хорошо, пока он не наткнулся на тему “Функции”.
# 
# Задание звучит так:
# Основная ветка программы, не считая заголовков функций, состоит из одной строки кода.
# 
# Это вызов функции test().
# В ней запрашивается на ввод целое число.
# Если оно положительное, то вызывается функция positive(),
# тело которой содержит команду вывода на экран слова "Положительное".
# 
# Если число отрицательное, то вызывается функция negative(),
# ее тело содержит выражение вывода на экран слова "Отрицательное".
# 
# Помогите Евгению и реализуйте такую программ

def positive():
    print('Положительное')

def negative():
    print('Отрицательное')

def test(num):
    if num > 0:
        positive()
    elif num < 0:
        negative()
    else:
        print('Ноль')

num = int(input('Введите число: '))
test(num)


print('Задача 3. Апгрейд калькулятора')

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия. 
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, 
# максимальную или минимальную цифру. 

#Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.

print('Задача 3. Апгрейд калькулятора')

def summ(number):
    sum_of_num = sum(int(digit) for digit in str(number))
    return sum_of_num

def max_num(number):
    max_digit = max(int(digit) for digit in str(number))
    return max_digit

def min_num(number):
    min_digit = min(int(digit) for digit in str(number))
    return min_digit

while True:
    number = input('Введите число (или "exit" для выхода): ')
    
    if number.lower() == 'exit':
        print('Выход из программы.')
        break
    
    if not number.isdigit():
        print('Пожалуйста, введите целое положительное число.')
        continue
    
    number = int(number)

    action = int(input('Выберите действие 1 - сумма цифр, 2 - максимальная цифра, 3 - минимальная цифра: '))
    
    if action == 1:
        result = summ(number)
        print(f'Сумма цифр числа {number} = {result}')
    elif action == 2:
        result = max_num(number)
        print(f'Максимальная цифра в числе {number} = {result}')
    elif action == 3:
        result = min_num(number)
        print(f'Минимальная цифра в числе {number} = {result}')
    else:
        print('Некорректный выбор действия. Пожалуйста, выберите 1, 2 или 3.')


print('Задача 4. Число наоборот')

# Вводится последовательность чисел,
# которая оканчивается нулём.
#
# Реализуйте функцию,
# которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.

# Пример:
# Введите число: 1234
# Число наоборот: 4321
# 
# Введите число: 1000
# Число наоборот: 0001
# 
# Введите число: 0
# Программа завершена!
# 
# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.
# 
# Введите число: 1230
# Число наоборот: 321
# 
# Кстати, нули, которые мы убрали, называются ведущими.

def reverse_number_recursive(number, reversed_number=0):
    if number == 0:
        return reversed_number
    return reverse_number_recursive(number // 10, reversed_number * 10 + number % 10)

while True:
    number = int(input('Введите число (0 для выхода): '))
    
    if number == 0:
        print('Программа завершена!')
        break
    
    reversed_number = reverse_number_recursive(number)
    print(f'Число наоборот: {reversed_number}')


print('Задача 5. Текстовый редактор')

# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы 
# и любой цифры в тексте (а не только буквы Ы как раньше).
# 
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
# 
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
# 
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
# 
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(text, letter, digit):
    count_letter = 0
    count_digit = 0

    for char in text:
        if char == letter:
            count_letter += 1
        if char == digit:
            count_digit += 1

    print(f'Количество букв "{letter}": {count_letter}')
    print(f'Количество цифр "{digit}": {count_digit}')

text = input('Введите текст: ')
letter = input('Какую букву ищем? ')
digit = input('Какую цифру ищем? ')

count_letters(text, letter, digit)



print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def calculate_gcd(first_number, second_number):
    """Функция для вычисления наибольшего общего делителя двух чисел."""
    while second_number != 0:
        first_number, second_number = second_number, first_number % second_number
    return first_number


# Ввод данных
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

# Вызываем функцию и выводим результат
result = calculate_gcd(first_number, second_number)
print(f'Наибольший общий делитель ({first_number}, {second_number}) = {result}')




print('Задача 7. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


def rock_paper_scissors():
    current_choice = 1

    while True:
        user_choice = input('Выберите: камень, ножницы или бумага (или введите "стоп" для выхода): ').capitalize()

        if user_choice == 'Стоп' or user_choice == 'Выход':
            print('Игра завершена!')
            break

        if user_choice != 'Камень' and user_choice != 'Ножницы' and user_choice != 'Бумага':
            print('Некорректный выбор, попробуйте снова.')
            continue

        if current_choice == 1:
            computer_choice = "Камень"
            current_choice = 2
        elif current_choice == 2:
            computer_choice = "Ножницы"
            current_choice = 3
        elif current_choice == 3:
            computer_choice = "Бумага"
            current_choice = 1

        print(f"Компьютер выбрал: {computer_choice}")

        if user_choice == computer_choice:
            print('Ничья!')
        elif (user_choice == 'Камень' and computer_choice == 'Ножницы') or \
             (user_choice == 'Ножницы' and computer_choice == 'Бумага') or \
             (user_choice == 'Бумага' and computer_choice == 'Камень'):
            print('Ты выиграл!')
        else:
            print('Ты проиграл!')


def guess_the_number():
    computer_number = 123

    while True:
        try:
            user_guess = int(input('Угадайте число! (или введите 0 для выхода): '))
        except ValueError:
            print('Пожалуйста, введите число.')
            continue

        if user_guess == 0:
            print('Игра завершена!')
            break
        elif user_guess == computer_number:
            print('Вы выиграли!')
            break
        else:
            print('Неправильно, попробуйте ещё раз.')


def main_menu():
    while True:
        try:
            user_choice = int(input('Выберите игру: 1 - Камень, ножницы, бумага.\n2 - Угадай число.\n3 - Выйти.\n'))
        except ValueError:
            print('Пожалуйста, выберите 1, 2 или 3.')
            continue

        if user_choice == 1:
            rock_paper_scissors()
        elif user_choice == 2:
            guess_the_number()
        elif user_choice == 3:
            print('Выход из игры.')
            break
        else:
            print('Некорректный выбор, попробуйте снова.')


main_menu()
