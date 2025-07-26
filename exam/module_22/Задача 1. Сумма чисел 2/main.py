# Во входном файле numbers.txt записано N целых чисел, которые могут быть разделены пробелами и концами строк. 
# Напишите программу, которая выводит сумму чисел во выходной файл answer.txt.

# Пример:

# Содержимое файла numbers.txt
#      2
# 2
#   2
#         2

# Содержимое файла answer.txt

# 8

import os

def find_nums(path):
    total = 0
    with open (path, 'r', encoding='utf-8') as input_file:
        for line in input_file:
             parts = line.strip().split()
             for part in parts:
                  if part.lstrip('-').isdigit():
                      total += int(part)
    return total


def create_nums(path, value):
    with open (path, 'w', encoding='utf-8') as output_file:
        output_file.write(f'{value}\n')
        
        
input_path = r'D:\Learning\Python\python_tasks\exams\module_22\Задача 1. Сумма чисел 2\numbers.txt'
output_path = r'D:\Learning\Python\python_tasks\exams\module_22\Задача 1. Сумма чисел 2\answer.txt'


result = find_nums(input_path)
create_nums(output_path, result)