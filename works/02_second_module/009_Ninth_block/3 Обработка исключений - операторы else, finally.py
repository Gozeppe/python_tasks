# Задача 1. Простая программа
# Напишите программу, которая открывает файл и записывает туда введённую пользователем строку. Используйте операторы try except else finally. 
# Обработайте возможные ошибки:

# Проблема при открытии файла.
# Нельзя преобразовать данные в целое.
# Неожиданная ошибка.
import os


def wrt_and_fnd(filename):
    file = None
    try:
        
     file = open(filename, "r+", encoding="utf-8")
     os.path.exists(filename)
     
    except FileNotFoundError:
     print("Ошибка: нет такого файла")
    except Exception as e:
     print(f'Неожиданная ошибка: {e}')
    else:
        try:
         user_input = int(input('Введите число: '))
        except ValueError:
            print('Число введите.')
        else:
         digit  = user_input % 10 
         dozen = user_input % 100 // 10
         file.write(str(f'Десятки - {dozen}\nЕдиницы - {digit}\n'))
        
    finally:
        
     if file is not None:
        file.close()

    
    
    

fil = r'D:\Learning\Python\python_tasks\works\02_second_module\009_Ninth_block\second_work.txt'

wrt_and_fnd(fil)
    
# Задача 2. Старая задача
# Возьмите любую задачу из домашнего задания, например, предыдущего модуля и оформите её решение в виде try except finally (можно ещё и else), 
# обрабатывая возможные ошибки.

# Посмотрев на то, что получилось, попробуйте ответить себе на такой вопрос: когда стоит использовать обработку исключений и когда она будет излишней?


def find_and_count(txt, output):
    dic_tol = {}
    filo = None
    filu = None
    try:
     filo = open(txt, 'r', encoding='cp1251')
    except FileNotFoundError:
        print('Нет такого файла')
    else:
        for line in filo:
            for char in line:
              if char.isalpha():
                    dic_tol[char] = dic_tol.get(char, 0) + 1
    finally:
        if filo is not None:
            filo.close()
    try:
     filu =  open(output, 'w', encoding='utf-8')
    except FileNotFoundError:
        print('Нет такого файла')
    else:
        for symb, blya in sorted(dic_tol.items(), key = lambda item : item[1], reverse=True ):
            filu.write(f'{symb} - {blya}\n')
    finally:
      if filo is not None:
          filo.close()
          
          
          
output = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 6. «Война и мир»\letter_stats.txt'
txt_file = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 6. «Война и мир»\voina-i-mir\voina-i-mir.txt'
find_and_count(txt_file, output)