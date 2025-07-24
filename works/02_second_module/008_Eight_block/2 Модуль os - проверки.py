# Задача 1. Иконки
# Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура его диска: папки одними иконками,
# файлы — другими. Поэтому ему нужен код, который поможет определить, какой тип иконки вставить.

# Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь 
# (на директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение. Если путь указывает на файл, 
# то также выведите его размер (сколько он весит в байтах). Обеспечьте контроль ввода: проверка пути на существование. 

 

# Подсказка: для вывода размера файла поищите соответствующий метод.

import os

full_p = ('E:\project\projects\Whispers\Whispers\log.txt')

if os.path.exists(full_p):
    print(True)
    
if os.path.isfile(full_p):
    print('Это файл')


if os.path.isdir(full_p):
    print('Это дериктория')

if os.path.islink(full_p):
    print('Это ссылка')


print(os.path.getsize(full_p), 'байт')

print('Размер файла:', os.path.getsize(full_p), 'байт')
    
    
    
    
# Пример 1:

# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py

# Это файл

# Размер файла: 605 байт

 

# Пример 2:

# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py

# Указанного пути не существует



# Задача 2. Поиск файла
# В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной директории. 
# Однако, как мы понимаем, файлов с таким названием может быть несколько.

# Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла, 
# проходит по всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.

 

# Пример:

# Ищем в: C:/Users/Roman/PycharmProjects/Skillbox

# Имя файла: lesson2


# Найдены следующие пути:

# C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py

# C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py

# C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py

# C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py

# C:/Users/Roman/PycharmProjects/Skillbox\Module19\lesson2.py

# C:/Users/Roman/PycharmProjects/Skillbox\Module20\lesson2.py

# C:/Users/Roman/PycharmProjects/Skillbox\Module21\lesson2.py

# C:/Users/Roman/PycharmProjects/Skillbox\Module22\lesson2.py


import os


fil_pat = r'D:\Learning\Python\python_tasks\works\02_second_module'
fil_name = '1.py'

def find_stuff(dirc):
    rt_stuff = []
    for root, dirs, files in os.walk(dirc):
        if fil_name in files:
           found_path = os.path.join(root, fil_name)
           rt_stuff.append([found_path])

    return rt_stuff

      
for path in find_stuff(fil_pat):
    print(path)
