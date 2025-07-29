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

output = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 6. «Война и мир»\letter_stats.txt'
txt_file = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 6. «Война и мир»\voina-i-mir\voina-i-mir.txt'
find_and_count(txt_file, output)