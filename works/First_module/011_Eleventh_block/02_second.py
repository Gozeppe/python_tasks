#  Задача 1. Возможности компьютера
#  В одной IT-компании тестируют возможности различных языков программирования, компиляторов и, конечно же, компьютеров. 
# Компания дала вам задачу понять, какое самое маленькое возможное число можно получить путём постоянного деления числа на 2. 
# Изначально число равно единице. Также, помимо самого числа, компания просит вывести количество делений. Реализуйте такую программу.

a = 1
count = 0

# Будем продолжать делить, пока результат деления отличается от 0
while a > 0:
    a /= 2
    count += 1
    print(f"Результат деления: {a}")

print(f"Количество делений: {count}")



#  Задача 2. Тестирование
#  Команде программистов отдали на тестирование новую модель суперкомпьютера. Для начала программисты решили проверить,
#  как у компьютера обстоят дела с вычислениями вещественных чисел.
#  Разработчики компьютера предупредили, что на входе он работает только с экспоненциальной формой числа.

# # Пользователь вводит число N в экспоненциальной форме, где мантисса всегда равна числу от 1 до 9, а порядок меньше нуля. 
# Также есть переменная Х, которая изначально равна единице. Посчитайте, сколько раз нужно прибавить N к Х, 
# чтобы оно перевалило за двойку.

#  Дополнительно: обеспечьте контроль ввода.

#  Пример 1:

#  Введите число в эксп. форме: 1e-3
#  Кол-во прибавлений: 1001
#  Пример 2:

#  Введите число в эксп. форме: 5.02e-1
#  Кол-во прибавлений: 2

# Контроль ввода экспоненциального числа
while True:
    try:
        n = float(input("Введите число в экспоненциальной форме: "))
        if n < 1e-9 or n >= 1:
            print("Число должно быть в экспоненциальной форме, где мантисса от 1 до 9, а порядок меньше нуля.")
        else:
            break
    except ValueError:
        print("Неверный ввод. Попробуйте еще раз.")

# Инициализация переменной X
X = 1
count = 0

# Прибавляем N к X, пока X не станет больше 2
while X <= 2:
    X += n
    count += 1

# Вывод результата
print(f"Количество прибавлений: {count}")



#  Задача 3. Урок информатики
#  На одном из уроков информатики учитель объяснял тему «Числа с плавающей точкой», но несколько учеников никак не могли понять, 
# почему эта точка «плавает» и как вообще выглядят числа в такой форме. Для наглядности учитель написал программу,
#  которая берёт число больше десяти и выводит его в формате плавающей точки.


#  Пользователь вводит положительное число x (x > 10). Напишите функцию, которая выводит его в формате плавающей точки, 
# то есть x = a *10 ** b, где 1 ≤ a < 10.

#  Пример 1:

#  Введите число: 16
#  Формат плавающей точки: x = 1.6 * 10 ** 1
#  Пример 2:

#  Введите число: 92345
#  Формат плавающей точки: x = 9.2345 * 10 ** 4

def float_format(x):
    # Определяем порядок (количество разрядов - 1)
    b = len(str(int(x))) - 1  # len(str(int(x))) возвращает количество цифр до десятичной точки
    # Вычисляем мантиссу
    a = x / (10 ** b)
    # Выводим результат
    print(f"Формат плавающей точки: x = {a} * 10 ** {b}")

# Контроль ввода
while True:
    try:
        x = float(input("Введите число больше 10: "))
        if x <= 10:
            print("Число должно быть больше 10. Попробуйте снова.")
        else:
            break
    except ValueError:
        print("Некорректный ввод. Введите числовое значение.")

# Вызов функции
float_format(x)