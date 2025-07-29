# Если в заказе есть цифра — это считается ошибкой (какой нормальный человек кладёт "1 яблоко" в сок?!)
# Нужно выбросить ошибку (raise ValueError) и записать её в orders_errors.log (с номером строки и содержимым заказа).
# Если заказ короче 4 символов (после удаления пробелов) — это подозрительно, и надо вызвать ошибку (raise ValueError) и тоже логировать.
# Все валидные заказы вывести на экран (например: “Заказ принят: апельсин”).
# В конце написать, сколько всего успешных заказов обработано.




def anal_cunt(inp, out):
    count_orders = 0
    try:
        with open(inp, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                
                 try:
                    if any(ch.isdigit() for ch in line):
                            print(f'Попалась цифра в сстроке {line}')
                            raise ValueError(f'В Этом заказе {line} цифра!')
                    for word in line.strip().split():
                     if len(word) < 4:
                      print(f'Подозрительно... {word} не подходит')
                      raise ValueError(f'Меньше 4 букв, странно, ')
                    
                 except ValueError as e:
                    with open(out, 'a', encoding='utf-8') as fil:
                         fil.write(f'{e} в строке {line_number}, \n')
                 else:
                    print(f'Заказ принят, {word}')
                    count_orders += 1
        print(f'Общее количество заказов: {count_orders}')
    except FileNotFoundError:
         print('Нет такого файла')




inp_path = r'D:\Learning\Python\python_tasks\works\02_second_module\009_Ninth_block\orders.txt'
out_path = r'D:\Learning\Python\python_tasks\works\02_second_module\009_Ninth_block\oders_errors.log'

anal_cunt(inp_path, out_path)