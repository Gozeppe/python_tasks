#Задача 1. Квадраты чисел
#Напишите программу, которая выводит квадраты чисел от 0 до 10. Для этого используйте цикл for и функцию range.

for numbers in range(11):
    result = numbers ** 2
    print(result)
    

#Задача 2. Кукушка
#Напишите программу, которая имитировала бы часы с кукушкой. В начале работы она спрашивает, который час, 
# а затем нужное количество раз пишет “Ку-ку!”.

co_hour = int(input('Который час? '))
for coco in range(co_hour):
    print('Ку-Ку!')
   

#Задача 3. Любовь с первой цифры (цикл for)
#Перепишите программу из прошлого модуля, используя цикл for.

#Паша очень любит математику. Настолько сильно, что у него по всей комнате висят всякие таблицы умножения, сложения, какие-то графики, формулы.
#  И теперь он захотел распечатать таблицу степеней двойки, у них как раз началась новая тема по информатике.

#Используя цикл for, выведите на экран для числа 2 его степени от 0 до 20.

base = 2
for exponent in range(21):
    result = base ** exponent
    print(f"{base}^{exponent} = {result}")