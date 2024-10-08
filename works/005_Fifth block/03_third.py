#Задача 1. Квадраты превратились в кубы
#Напишите программу, которая выводит кубы чисел (число в третьей степени), лежащих в диапазоне от 1 до 10.

#Результат:

1
8
27
64
125
216
343
512
729
1000

for number in range(1, 11):
    cube = number ** 3
    print(cube)

#Задача 2. Сумма чисел
#Напишите программу, где пользователь вводит любые два целых положительных числа. А программа суммирует все числа в диапазоне от первого до второго. 
# Гарантируется, что первое введённое число всегда меньше второго.

#Пример:

#Введите первое число: 5
#Введите второе число: 10
#Сумма чисел от 5 до 10 равна 45

first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

total_sum = 0

for num in range(first_num, second_num + 1):
    total_sum += num

print(f'Сумма чисел от {first_num} до {second_num} равна {total_sum}')

#Задача 3. Поел — можно и поспать, поспал — можно и поесть
#Напишите программу, разобранную в уроке.

#У Саши интересный режим сна: он может проснуться когда угодно, хоть ночью, но засыпает всегда до того, как наступит полночь, обычно в 23 часа.
#  А ещё он очень любит поесть. Он ест каждый час и если съедает больше 2000 калорий, то он просто падает спать. 
# Напишите программу, которая поможет Саше понять, всё ли с ним хорошо. Для этого нужно посчитать, 
# сколько он всего съест калорий и сколько часов будет бодрым.

wake_hour = int(input('Когда встанешь?'))
awake_hour = 0
calories = 0

for hour in range (wake_hour, 23):
    hour_eat = int(input('Который час?'))
    hour_calories = int(input('Сколько калорий потреблено?'))
    calories += hour_calories 
    if calories >= 2000:
     print(f'Наелся и спит')
     break
    awake_hour += 1
print(f'Калорий потреблено {calories}')
print(f'Прободорствовал {awake_hour} часов')
