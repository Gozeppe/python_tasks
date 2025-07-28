def find_and_reverse(input_file, output_file):
    dici_tolst = {}
    with open(input_file, 'r', encoding='cp1251') as file:
        for line in file:
         for i in range(len(line) - 2):   # перебираем индексы, чтобы брать срез из 3 символов
          
          trigram = line[i:i+3]
          
          if trigram.isalpha():
              dici_tolst[trigram] = dici_tolst.get(trigram, 0) + 1
    with open(output_file, 'w', encoding='utf-8') as fil:
        top_10 = sorted(dici_tolst.items(), key = lambda item: item[1], reverse=True)[:10]
        for trigram, count in top_10:
            fil.write(f'{trigram} {count}\n')
            
inpit = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 6. «Война и мир»\voina-i-mir\voina-i-mir.txt'
outpit = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 6. «Война и мир»\voina-i-mir\trigram.txt'

find_and_reverse(inpit, outpit)

 #from collections import Counter

# counter = Counter()
# ...считаешь частоты

# for trigram, count in counter.most_common(10):
#     print(trigram, count)