# Задача 2. Всё в одном
# Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город, и там у него случилась беда: его диск пришлось отформатировать, 
# а доступ в интернет отсутствует. Остался только телефон с мобильным интернетом.
# Так как со связью (и с памятью) проблемы, друг попросил вас скинуть одним файлом все решения и скрипты, которые у вас сейчас есть.

# Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic в файл scripts.txt, разделяя код строкой из 40 символов *. 

 

# Пример содержимого файла scripts.txt:

# import platform

# import sys

 

# info = 'OS info is \n{}\n\nPython version is {} {}'.format(

#     platform.uname(),

#     sys.version,

#     platform.architecture(),

# )

# print(info)

 

# with open('os_info.txt', 'w', encoding='utf8') as file:

#     file.write(info)

# ****************************************

# print("Введите первую точку")

# x1 = float(input('X: '))

# y1 = float(input('Y: '))

# print("\nВведите вторую точку")

# x2 = float(input('X: '))

# y2 = float(input('Y: '))

 

# print("Уравнение прямой, проходящей через эти точки:")

# x_diff = x1 - x2

# y_diff = y1 - y2

# if x_diff == 0:

#     print("x = ", x1)

# elif y_diff == 0:

#     print("y = ", y1)

# else:

#     k = y_diff / x_diff

#     b = y2 - k * x2

#     print("y = ", k, " * x + ", b) 


import os
all_scripts = []

fls = 'D:\Learning\Python\python_tasks\works'
for root, dirs, files in os.walk(fls):
    for file in files:
        if file.endswith('.py'):
            full_path = os.path.join(root, file)
            
            with open (full_path, encoding= 'utf-8') as f:
                code = f.read()
                all_scripts.append(code)
                all_scripts.append('*' * 40)
                
with open('scripts.txt', 'w', encoding='utf-8') as result:
    result.write('\n'.join(all_scripts)) 
            