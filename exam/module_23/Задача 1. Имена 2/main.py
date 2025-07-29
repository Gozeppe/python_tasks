

def find_and_count(input_file, error_msg):
    total = 0
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
           for line_number, line in enumerate(file, 1):
                try:
                    if any(ch.isdigit() for ch in line):
                            print(f'Попалась цифра в сстроке {line}')
                            raise ValueError(f'В Этом заказе {line} цифра!')
                    total += len(line.strip())
                    for word in line.strip().split():
                        if len(word) < 3:
                         raise ValueError(f'В строке {line_number} меньше 3-ех символов')
                
                    
                    
                except ValueError as e:
                    with open(error_msg, 'a', encoding='utf-8') as fil:
                         fil.write(f'{e} в строке {line_number} \n')
                         print(e)
    except FileNotFoundError:
        print('Нет такого файла')       
    else:
        print(f'Общее количество символов: {total}')
        
inpi = r'D:\Learning\Python\python_tasks\exam\module_23\Задача 1. Имена 2\people.txt'
err_msg = r'D:\Learning\Python\python_tasks\exam\module_23\Задача 1. Имена 2\error_msg.txt'

find_and_count(inpi, err_msg)