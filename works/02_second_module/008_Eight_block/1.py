# Задача для закрепления:
# Задача:
# У тебя есть текстовый файл (любой, хоть "Война и мир").

# Найди все слова, которые встречаются ровно один раз во всём тексте (учитывай регистр и все буквы).

# Словом считаем любую последовательность символов, разделённую пробелом или переносом строки.

# Выведи эти слова (одиночки) в файл или на экран — каждое на своей строке, в любом порядке.
from collections import Counter
inp_path = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 6. «Война и мир»\voina-i-mir\voina-i-mir.txt'
out_path = r'D:\Learning\Python\python_tasks\works\02_second_module\008_Eight_block\test.txt'

def find_only(inp, out):
 words = []
 counter = Counter()
 with open(inp, 'r', encoding='cp1251') as file:
        for line in file:
            for word in line.split():
                counter[word] += 1
        for word, count in counter.items():
                    if count == 1:
                        words.append(word)
                    
 with open(out, 'w', encoding='utf-8') as fil:
     for wordkin in words:
         print(f'{wordkin}\n')
         fil.write(f'{wordkin}\n')
         
find_only(inp_path, out_path)

# from collections import Counter

# counter = Counter()
# with open('file.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         for word in line.split():
#             counter[word] += 1

# for word, count in counter.items():
#     if count == 1:
#         print(word)
