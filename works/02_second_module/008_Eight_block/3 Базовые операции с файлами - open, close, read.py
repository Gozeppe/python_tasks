# дача 1. Результаты
# Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей. Файл первой группы (group_1.txt) находится в папке task, 
# файл второй группы (group_2.txt) — в папке Additional_info.


 

# Содержимое файла group_1.txt

# Бобровский Игорь 10

# Дронов Александр 20

# Жуков Виктор 30

 

# Содержимое файла group_2.txt

# Павленко Геннадий 20

# Щербаков Владимир 35

# Marley Bob 15

 

# На экран нужно было вывести сумму очков первой группы, затем разность очков опять же первой группы и напоследок — произведение очков уже второй группы. 

# Программист оказался не очень опытным, писал код наобум и даже не стал его проверять. И оказалось, этот код просто не работает. Вот что он написал:

 

# file = open('E:\task\group_1.txt', 'read')

# summa = 0

# for i_line in file:

#     info = i_line.split()

#     summa += info[2]

# file = open('E:\task\group_1.txt', 'read')

# diff = 0

# for i_line in file:

#     info = i_line.split()

#     diff -= info[2]

# file_2 = open('E:\task\group_2.txt', 'read')

# compose = 0

# for i_line in file:

#     info = i_line.split()

#     compose *= info[2]

# print(summa)

# print(diff)

# print(compose)

import os

total = 0
razn = 0
sum_of_fls = 1
group_1 = []

with open(r'D:\task\group_1.txt', 'r', encoding='utf-8') as file:
    
    for i_line in file:
        num = i_line.strip().split()
        if len(num) >= 3 and num[-1].isdigit():
         total += int(num[2])
         group_1.append(int(num[2]))
print(total)    

if len(group_1) >= 3:
    razn = group_1[0] - group_1[1] - group_1[2]
print("Разность:", razn)


    
with open(r'D:\task\additional_info\group_2.txt', 'r', encoding='utf-8') as file_2:
    
    for i_comp in file_2:
        num_3 = i_comp.strip().split()
        if len(num_3) >= 3 and num_3[-1].isdigit():
            sum_of_fls *= int(num_3[2])
            
print(sum_of_fls)

# Исправьте код для решения поставленной задачи. Для проверки результата создайте необходимые папки 
# (task, Additional_info, Dont touch me) на своём диске в соответствии с картинкой и также добавьте файлы group_1.txt и group_2.txt.



# Задача 2. Поиск файла 2
# Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только программисту. Таким образом, с ними можно работать точно так же,
# как и с обычными текстовыми файлами.

# Используя функцию поиска файла из предыдущего урока, реализуйте программу,
#   которая находит внутри указанного пути все файлы с искомым названием и выводит на экран текст одного из них (выбор можно сгенерировать случайно).

# Подсказка: можно использовать, например, список для сохранения найденного пути.

import random

find_lst = []

usr_path = input('Введите путь: ')
usr_fil = input('Введите название файла: ')



    
    
for root, dict, files in os.walk(usr_path):
    for file in files:
        if file == usr_fil:
            full_path = os.path.join(root, file)
            find_lst.append(full_path)
            


    
if find_lst:
    selected = random.choice(find_lst)
    
    with open(selected, 'r', encoding='utf-8') as fil:
     print(fil.read())