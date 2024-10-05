#Задача 1. Надоедливый заказчик

#Нашему заказчику нужно, чтобы фраза «Я — программист!» выводилась на экран столько раз, сколько он сам этого захочет.

#Напишите программу, которая запрашивает число — количество строчек с фразой «Я — программист!» — и столько же раз выводит на экран эту фразу.
#  Для решения задачи используйте переменную-счётчик,
#  которая увеличивается на единицу до тех пор, пока не будет выведено нужное количество строчек.



count = int(input("How many times do i need to type 'I'm a programmer?': "))
counter = 0
while counter < count:
    print("I'm a programmer")
    counter += 1
print('Loop is done')

#Задача 2. Напоминалка

#У Евгения много работы, а ещё он очень забывчивый. Иногда он забывает о какой-нибудь важной встрече, 
# и ему приходится выслушивать критику от начальства. Напишите для него программу-напоминалку. 
# В самом начале программа спрашивает, сколько раз ему напомнить, а затем нужное количество раз выводит: «Вы хотели не забыть о чём-то».

counter_Eug = 0
reminder = int(input('How many times do i need to remind you?: '))

while counter_Eug < reminder:
    print('You wanted to be reminded of something')
    counter_Eug += 1

#Задача 3. Рыбалка

#Наши прекрасные родственники удачно сходили на рыбалку. 
# Настолько, что ходили мешком перетаскивать рыбу с берега в машину целых n раз. 
# Каждый мешок они взвешивали на электронных весах (все мешки весили по-разному). 
# Напишите программу для весов, которая считает суммарный вес мешков и выводит его на экран.

sack_count = int(input('How many sacks?: '))

total_weight = 0  # Переменная для хранения суммарного веса мешков
counter = 0  # Счётчик для отслеживания количества обработанных мешков

while counter < sack_count:
    sack_weight = float(input(f'Enter the weight of sack {counter + 1}: '))
    total_weight += sack_weight  # Добавляем вес мешка к общей сумме
    counter += 1  # Увеличиваем счётчик на 1

# Выводим суммарный вес
print(f'The total weight of all sacks is: {total_weight} kg')