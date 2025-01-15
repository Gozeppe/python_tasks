print('Задача 1. Космическая еда')

# Ваш космический корабль потерпел крушение на пустынной планете. Еда здесь не растёт, но вы спасли из обломков 100-килограммовый мешок гречки. Из прошлого опыта вы знаете, что если будете экономно питаться, то у вас будет уходить по четыре килограмма гречки в месяц.

# Чтобы прикинуть гречневый бюджет, вы решили написать программу, которая выведет информацию о том, сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее, пока она не закончится. Используйте цикл for.

initial_grain_weight = 100 
monthly_consumption = 4     

for month in range(1, initial_grain_weight // monthly_consumption + 2):
    remaining_grain_weight = initial_grain_weight - monthly_consumption * (month - 1)
    if remaining_grain_weight < 0:
        remaining_grain_weight = 0
    print(f'Через {month} месяц(а) останется {remaining_grain_weight} кг гречки.')

print('Расчёты завершены.')


print('Задача 2. Долги')

# «МирПрогБанк» наконец-то разделил законопослушных граждан и должников и поместил их в разные базы. Но банк не торопится сильно давить на неплательщиков. Операторам банка дали задание позвонить каждому пятому должнику из списка (нумерация начинается с нуля) и уточнить, какую сумму каждый из них задолжал банку.

# Напишите программу, которая получает данные о количестве должников, а затем спрашивает у каждого пятого (начиная с нуля) его долг. В конце выводится общая сумма долгов.

# Пример 1
# Введите количество должников: 13
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Должник с номером 10
# Сколько должны? 2000
# Общая сумма долга: 8000

# Пример 2
# Введите количество должников: 10
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Общая сумма долга: 6000


number_of_debtors = int(input('Введите количество должников: '))

total_debt = 0

for debtor_number in range(0, number_of_debtors, 5):
    print(f'Должник с номером {debtor_number}')
    debt_amount = int(input('Сколько должны? '))
    total_debt += debt_amount

print(f'Общая сумма долга: {total_debt}')


print('Задача 3. Таймер для микроволновых печей')

# Мы разрабатываем микропрограмму — таймер обратного отсчета для микроволновых печей. Некоторым пользователям не нравится пищащий звук.
# Есть задача убрать звук по готовности и заменить его сообщением на LED-экране. В нашем случае будем выводить в консоль сообщение с обратным отсчетом в секундах от “reverse_timer” до момента готовности, то есть «0» секунд, и спрашивать пользователя, готов ли он забрать еду.

# Пользователь в любой момент может прервать режим разогрева, введя «1» (то есть ответить «Да, еда готова»), тогда программа выводит на экран сообщение «Ваша еда готова, можете забрать» и показывает, на какой секунде был прерван таймер.
# Если пользователь отвечает «0», что равноценно «Нет», то таймер уменьшается. Когда он достигнет «0» секунд, выводим сообщение «Ваша еда готова, осторожно горячo!»

# В данном задании используем цикл for.
# “reverse_timer” – переменная счетчик, значение которой запрашиваем у пользователя через функцию ввода input.

# 1) Задайте время до обнуления таймера.
# 2) Используйте цикл for.
# 3) На каждой итерации задавайте персонажу вопрос, хочет ли он сейчас остановить разогрев или нет.

print('Таймер обратного отсчета')

reverse_timer = int(input('Введите время таймера в секундах: '))

for remaining_time in range(reverse_timer, -1, -1):
    print(f'Осталось {remaining_time} секунд')
    user_input = input('Готовы забрать еду? (0 - нет, 1 - да): ')
    if user_input == '1':
        print(f'Ваша еда готова, можете забрать. Таймер был прерван на {remaining_time} секундe.')
        break
else:
    print('Ваша еда готова, осторожно горячo!')


print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
c = int(input('Введите значение c: '))

sum_of_multiples = 0
count_of_multiples = 0

for number in range(a, b + 1):
    if number % c == 0:
        sum_of_multiples += number
        count_of_multiples += 1

if count_of_multiples > 0:
    average = sum_of_multiples / count_of_multiples
else:
    average = 0

print(f'Среднее арифметическое чисел, кратных {c}, в отрезке [{a}; {b}] равно {average}')

print('Задача 5. Функция')

# Перед изучением функций из программирования Саша решил оживить свои знания о функциях математики. Помогите Саше написать программу, которая будет считать значение функции в каждой точке отрезка с нужным шагом, начиная с конца).
# Напишите программу, которая получает на вход начало и конец отрезка, а также шаг (отрицательный), а затем высчитывает функцию y в каждой точке отрезка и выводит ответ на экран с нужным шагом, начиная с конца.

# Сама функция выглядит так:
# y = x**3 + 2*x**2 - 4*x + 1

# Пример:
# 
# Введите начало отрезка: -2
# Введите конец отрезка: 2
# Введите шаг: -1
# В точке 2 функция равна 9
# В точке 1 функция равна 0
# В точке 0 функция равна 1
# В точке -1 функция равна 6
# В точке -2 функция равна 9

# Учтите, что пользователь может ввести некорректные диапазоны и вам нужно их скорректировать так, 
# чтобы вывод был при любых вводных.

start = int(input('Введите начало отрезка: '))
end = int(input('Введите конец отрезка: '))
step = int(input('Введите шаг: '))

if step >= 0:
    step = -step

if start < end:
    start, end = end, start

for x in range(start, end - 1, step):
    y = x**3 + 2*x**2 - 4*x + 1
    print(f'В точке {x} функция равна {y}')


print('Задача 6. Стипендия')

# Ежемесячная стипендия студента составляет educational_grant рублей, а расходы на проживание превышают стипендию и составляют expenses рублей в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца. Обратите внимание, что каждый месяц цены увеличиваются на 3% относительного прошлого месяца.

# Составьте программу расчёта суммы денег, которую необходимо получить у родителей один раз в начале обучения, чтобы можно было прожить учебный год (десять месяцев), используя только эти деньги и стипендию.

# Пример:

# Введите стипендию: 10000
# Введите расходы на проживание: 12000

# 1. месяц траты 12000 не хватает 2000
# 2. месяц траты 12360.0 не хватает 4360.0
# 3. месяц траты 12730.8 не хватает 7090.8
# 4. месяц траты 13112.7 не хватает 10203.52
# 5. месяц траты 13506.1 не хватает 13709.63
# 6. месяц траты 13911.2 не хватает 17620.92
# 7. месяц траты 14328.6не хватает 21949.55
# 8. месяц траты 14758.4 не хватает 26708.03
# 9. месяц траты 15201.2 не хватает 31909.27
# 10. месяц траты 15657.2 не хватает 37566.55

# Нужно попросить у родителей 37566.55 рублей

educational_grant = float(input('Введите стипендию: '))
expenses = float(input('Введите расходы на проживание: '))

total_needed = 0
monthly_expenses = expenses
cumulative_deficit = 0

for month in range(1, 11):
  deficit = monthly_expenses - educational_grant
  cumulative_deficit += max(deficit, 0)

  print(
    f'{month}. месяц траты {monthly_expenses:.1f} не хватает {cumulative_deficit:.1f}'
  )

  monthly_expenses *= 1.03

print(f'\nНужно попросить у родителей {cumulative_deficit:.2f} рублей')


print('Задача 7. Сумма ряда')

# Дано натуральное число N. Напишите программу для вычисления суммы N элементов последовательности по формуле 
# (-1)**n * 1/(2**n), где n — это порядковый номер элемента (расчёт начинается с нуля).

# Примеры расчётов

# При N = 4 элементы выражения будут равны:
# n = 0 
# elem = (−1) ** 0 * (½) ** 0 = 1
# n = 1
# elem = (−1) ** 1 * (½) ** 1 = (−½)
# n = 2
# elem = (−1) ** 2 * (½) ** 2 = ¼
# n = 3
# elem = (−1) ** 3 * (½) ** 3 = (−⅛)
# Сумма равна:
# s=1- 12+14-18 = 5/8 = 0,625

# При N = 6 элементы выражения будут равны:
# n = 0 
# elem = (−1) ** 0 * (½) ** 0 = 1
# n = 1
# elem = (−1) ** 1 * (½) ** 1 = (−½)
# n = 2
# elem = (−1) ** 2 * (½) ** 2 = ¼
# n = 3
# elem = (−1) ** 3 * (½) ** 3 = (−⅛)
# n = 4
# elem = (−1) ** 4 * (½) ** 4 = (1/16)
# n = 5
# elem = (−1) ** 5 * (½) ** 5 = (−1/32)
# Сумма равна:
# s = 1 − ½ + ¼ − ⅛ + 1/16 − 1/32 = 21/32 = 0,65625

# P. S. Не стоит выполнять расчёты каждого элемента вручную, используйте цикл.

N = int(input("Введите значение N: "))

sum_sequence = 0
sum_expression = ""
fraction_parts = []

for n in range(N):
    numerator = (-1) ** n
    denominator = 2 ** n
    element = numerator / denominator
    sum_sequence += element

    if n == 0:
        fraction_parts.append(f"{numerator}/{denominator}")
    else:
        if numerator > 0:
            fraction_parts.append(f"+ {numerator}/{denominator}")
        else:
            fraction_parts.append(f"- {abs(numerator)}/{denominator}")

    print(f'n = {n}')
    print(f'elem = (-1) ** {n} * (½) ** {n} = {numerator}/{denominator}')

sum_expression = " ".join(fraction_parts).replace(" + -", " - ")

final_numerator = 0
final_denominator = 1
current_denominator = 1

for i in range(N):
    current_numerator = (-1) ** i
    current_denominator = 2 ** i
    final_numerator = final_numerator * current_denominator + current_numerator * final_denominator
    final_denominator *= current_denominator

while final_numerator % 2 == 0 and final_denominator % 2 == 0:
    final_numerator //= 2
    final_denominator //= 2

if final_denominator == 1:
    formatted_sum = f"{final_numerator}"
else:
    formatted_sum = f"{final_numerator}/{final_denominator}"

print('Сумма равна:')
print(f's={sum_expression} = {formatted_sum} ={sum_sequence:.6f}')


print('Задача 8. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
#
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
#
#
# Пример 1:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
#
# Пример 2:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBBGBBG
#
# Пример 3:
#
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))

if abs(boys - girls) > 2:
    print("Нет решения")
else:
    result = ""

    if boys >= girls:
        major_char = 'B'
        minor_char = 'G'
        major_count = boys
        minor_count = girls
    else:
        major_char = 'G'
        minor_char = 'B'
        major_count = girls
        minor_count = boys

    for _ in range(max(boys, girls)):
        if major_count > 0:
            result += major_char
            major_count -= 1
        if minor_count > 0:
            result += minor_char
            minor_count -= 1

        if major_count > minor_count and major_count > 0:
            result += major_char
            major_count -= 1

    print(result)
