
# Задача 1. Имена
# В базе данных одной компании есть баг (или, может быть, фича): если ввести туда имя сотрудника меньше чем из трёх букв, то база сломается и упадёт. 
# Как компания принимает на работу людей, например, с китайскими именами, непонятно.

# Дан файл people.txt, в котором построчно хранится N имён пользователей. 

# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму. 
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка, и программа завершается.

# Содержимое файла people.txt:

# Петя

# Ян

# Маша

# Ева

# Дмитрий

# Анастасия


def find_crew(inp_fil):
    sum = 0
    try:
        with open(inp_fil, 'r', encoding='utf - 8') as file:
            for line in file:
                name = line.strip()
                if not name:
                    continue
                if len(name) < 3:
                    raise ValueError(f'Имя "{name}" коротковато, брат')
                for sym in name:
                     sum += len(sym.strip())
                print(f'{name} - {sum}')
        
    except FileNotFoundError:
        print('Не найден файл, друг')
        
        
fil = r'D:\Learning\Python\python_tasks\works\02_second_module\009_Ninth_block\people.txt'

find_crew(fil)

# Задача 2. Логирование
# Возможно, вы замечали, что некоторые программы не просто выдают ошибку и закрываются, но и записывают эту ошибку в файл. 
# Таким образом проще сформировать отчёт об ошибках, а значит, программисту будет проще их исправить. Это называется логированием ошибок.

# Дан файл words.txt, в котором построчно записаны слова. Необходимо определить количество слов, из которых можно получить палиндром (привет предыдущим модулям).
# Если в строке встречается число, то программа выдаёт ошибку ValueError и записывает эту ошибку в файл errors.log


def find_poly(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            for line in file:
                for word in line.strip().split():  # <-- по словам, а не по буквам!
                    try:
                        if any(ch.isdigit() for ch in word):
                            print(f'Попалась цифра в слове {word}')
                            raise ValueError(f'В слове {word} цифра!')
                        if word == word[::-1]:
                            print(f'Клёво, чувак! слово {word} палиндром')
                        else:
                            print(f'Чеееел, слово {word} не палиндром...')
                    except ValueError as e:
                        with open(output_path, 'a', encoding='utf-8') as fil:
                            fil.write(f'{e}\n')    
    except FileNotFoundError:
        print('Нет такого пути')
    finally:
        print('Прошлись по всем словам')
