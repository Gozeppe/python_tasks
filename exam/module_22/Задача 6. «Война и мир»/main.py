
    
def find_and_count(txt, output):
    dic_tol = {}
    with open(txt, 'r', encoding='cp1251') as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    dic_tol[char] = dic_tol.get(char, 0) + 1
    
    with open(output, 'w', encoding='utf-8') as fil:
        for symb, blya in sorted(dic_tol.items(), key = lambda item : item[1], reverse=True ):
            fil.write(f'{symb} - {blya}\n')


output = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 6. «Война и мир»\letter_stats.txt'
txt_file = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 6. «Война и мир»\voina-i-mir\voina-i-mir.txt'
find_and_count(txt_file, output)