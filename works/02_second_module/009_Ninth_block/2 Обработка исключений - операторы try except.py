# Задача 1. Пятый элемент
# В курсе по программированию студенту дали простую задачу: умножить константу (число 42) на пятый элемент строки, введённой пользователем. Вот код студента:

 

# BRUCE_WILLIS = 42

 

# input_data = input('Введите строку: ')

# leeloo = int(input_data[4])

# result = BRUCE_WILLIS * leeloo

# print(f'- Leeloo Dallas! Multi-pass № {result}!')

 

# Модифицируйте этот код, обработав исключения для произвольных входных параметров:

# ValueError — невозможно преобразовать к числу,
# IndexError — выход за границы списка,
# остальные исключения.
# Для каждого типа исключений выведите на консоль соответствующее сообщение.

BRUCE_WILLIS = 42

 
try:
 input_data = input('Введите строку: ')

 leeloo = int(input_data[4])

 result = BRUCE_WILLIS * leeloo

 print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print('Указана не строка, укажи сьтроку, пятый элемент строки должен быть числом!')
except IndexError:
    print('За границы спискв вышел!')
except Exception as error:
 print(f'❌ Unexpected Error: {error}')

# Задача 2. Возраст
# Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.

# Напишите программу, которая считывает файл, даёт имя для каждого возраста (можно просто использовать буквы алфавита) 
# и выводит результат в новый файл result.txt в формате «имя — возраст». Программа должна обрабатывать следующие ошибки и выводить сообщение на экран:

# Попытка создания файла, который уже существует.
# На чтение ожидался файл, но это оказалась директория.
# Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
# При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.

names = ['Иван', 'Петя', 'Маша', 'Оля', 'Джон', 'Лариса', 'Борис', 'Кира', 'Антон', 'Грета']

def find_and_do(input_path, output_path):
    try:
      with open(input_path, 'r', encoding="utf-8") as file:
          with open(output_path, 'x', encoding='utf-8') as fil:
           for name, age in zip(names, file):
            try:
                age_value = int(age.strip())
                if age_value < 0:
                    raise ValueError
                fil.write(f'{name} — {age_value}\n')
            except (TypeError, ValueError):
             print(f'Неверный тип данных - {age.strip()}')

         
            
        
         
    except FileNotFoundError:       
     print('На чтение ожидался файл, а оказалсь дериктория!')
    except IsADirectoryError:
     print('На чтение ожидался файл, а оказалась директория!')
    except FileExistsError:
     print('файл уже существует!')
    


inpit = r'D:\Learning\Python\python_tasks\works\02_second_module\009_Ninth_block\ages.txt'
outpit = r'D:\Learning\Python\python_tasks\works\02_second_module\009_Ninth_block\result.txt'

find_and_do(inpit,outpit)