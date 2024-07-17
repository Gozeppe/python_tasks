print('Задача 1. Фруктовый сад')

#Маша проводит исследования корреляции размеров фруктов в зависимости от их расположения на участке. Она взяла яблоко, грушу и персик диаметрами 8, 5 и 3 сантиметра соответственно и вычислила коэффициент зависимости по своей формуле.

#Реализуйте программу, которая вычисляет значение выражения


#где a, b и c — переменные, в которых лежат числа 8, 5 и 3 соответственно. Выведите результат на экран.

a = 8
b = 5
c = 3

apple = a
pear = b
peach = c

do_math = ((a / (b + c)) - a) / c
print(do_math)

print('Задача 2. Автобус или метро?')

#Для расчёта эффективности потраченных денег на метро и автобус Никита использует следующую формулу:


#В общем, не спрашивайте. Он написал программу для подсчёта формулы, но она почему-то не работает.

bus = 5
metro = 3
result = (6 + (10 - bus)** 2) / (metro + 1) + 132 / (2 + bus)
print(result)
#Скопируйте программу в редактор, исправьте выражение и убедитесь в правильности её работы. Правильный ответ: 26.607142857142858



print('Задача 3. Сложные степени')

#Говорят, если в 22:31:49 посчитать на Python значение определённого выражения, то спустя год станешь очень хорошим программистом. Давайте проверим это утверждение.



#1. Создайте переменную и запишите в неё следующее математическое выражение:


#2. Затем выведите значение переменной на экран. Ответ должен быть равен 378652.3611111111.

#3. Будьте внимательны со скобками, особенно с делением числителя на знаменатель.

do_math_long = (-3 + (8**2 - 12) * 4**(3**2)) / (2 * 18)
print(do_math_long)
#Подсказка

#Приоритет операций в python не отличается от приоритета, принятого в алгебре.

#Операции выполняются в следующем порядке

#Операции в скобках (a + b)

#Операции возведения в степень a**b

#Операции умножения и деления a * b

#Операции сложения и вычитания a + b - c

#Операции унарных плюсов и минусов -4

#Приоритеты всех операций вы сможете найти по ссылке Приоритет операций

#При равенстве приоритетов операции выполняются слева направо.



#При вычислении выражений с числителем и знаменателем, записанных в виде дробей будьте внимательны к тому, что весь числитель нужно разделить на весь знаменатель.

#Для этого можно отдельно вычислить числитель и отдельно знаменатель, а потом разделить числитель на знаменатель, либо поместить числитель и знаменатель в скобки.