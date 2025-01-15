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
  for number in range(1, numbers + 1):
    summ += number
  print("Я знаю, что сумма чисел от 1 до", numbers, "равна", summ)


user_number = int(input("Введите число "))
calculate_and_output_sum_numbers(user_number)


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


def positive_digit():
  print('Положительное')


def negative_digit():
  print('Отрицательное')


def classify_number(number):
  if number > 0:
    positive_digit()
  elif number < 0:
    negative_digit()
  else:
    print('Ноль')


user_input = int(input('Введите число: '))
classify_number(user_input)



print('Задача 3. Апгрейд калькулятора')

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия.
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру.

#Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.


def calculate_sum(num):
  """Считает сумму цифр числа"""
  return sum(int(digit) for digit in str(num))


def find_max_digit(num):
  """Находит максимальную цифру в числе"""
  return max(int(digit) for digit in str(num))


def find_min_digit(num):
  """Находит минимальную цифру в числе"""
  return min(int(digit) for digit in str(num))


while True:
  user_input = input('Введите число (или "exit" для выхода): ')

  if user_input.lower() == 'exit':
    print('Выход из программы.')
    break

  if not user_input.isdigit():
    print('Пожалуйста, введите целое положительное число.')
    continue

  number_input = int(user_input)

  action_choice = input(
    'Выберите действие 1 - сумма цифр, 2 - максимальная цифра, 3 - минимальная цифра: '
  )

  if action_choice == '1':
    result = calculate_sum(number_input)
    print(f'Сумма цифр числа {number_input} = {result}')
  elif action_choice == '2':
    result = find_max_digit(number_input)
    print(f'Максимальная цифра в числе {number_input} = {result}')
  elif action_choice == '3':
    result = find_min_digit(number_input)
    print(f'Минимальная цифра в числе {number_input} = {result}')
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
  return reverse_number_recursive(number // 10,
                                  reversed_number * 10 + number % 10)


while True:
  value = int(input('Введите число (0 для выхода): '))

  if value == 0:
    print('Программа завершена!')
    break

  reversed_number = reverse_number_recursive(value)
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


def count_symbols(text, letter, digit):
  count_letter = 0
  count_digit = 0

  for char in text:
    if char == letter:
      count_letter += 1
    if char == digit:
      count_digit += 1

  print(f'Количество букв "{letter}": {count_letter}')
  print(f'Количество цифр "{digit}": {count_digit}')


user_text = input('Введите текст: ')
letter_find = input('Какую букву ищем? ')
digit_find = input('Какую цифру ищем? ')


count_symbols(user_text, letter_find, digit_find)



print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел


def calculate_gcd(first_number, second_number):
  while second_number != 0:
    first_number, second_number = second_number, first_number % second_number
  return first_number


first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

result = calculate_gcd(first_num, second_num)
print(
  f'Наибольший общий делитель ({first_num}, {second_num}) = {result}')



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
        user_choice = input(
            'Выберите: камень, ножницы или бумага (или введите "стоп" для выхода): '
        ).capitalize()

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
            user_guess = int(
                input('Угадайте число! (или введите 0 для выхода): '))
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
            user_choice = int(
                input(
                    'Выберите игру: 1 - Камень, ножницы, бумага.\n2 - Угадай число.\n3 - Выйти.\n'
                ))
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
