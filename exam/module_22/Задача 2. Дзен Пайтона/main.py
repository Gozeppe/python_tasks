import os

def find_and_reverse(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8' ) as input_file:
        lines = input_file.readlines()
            
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for line in lines[::-1]:
         output_file.write(line)
    return output_file

inp_path = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 2. Дзен Пайтона\zen.txt'
out_path = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 2. Дзен Пайтона\rev_zen.txt'

find_and_reverse(inp_path, out_path)
            