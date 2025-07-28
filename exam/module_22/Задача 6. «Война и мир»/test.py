text = "Привет, мир! 2024. Hello world! За буквы отвечаем."
dici = {}

for char in text:
    if char.isalpha():
        dici[char] = dici.get(char, 0) + 1
      
for char, num in sorted(dici.items(), key = lambda item: item[1], reverse=True):
    print(f'{char} {num}')
    
    
def find_and_find(input_path, output_path):
    toslt = {}
    with open(input_path, 'r', encoding='cp1251') as file:
        for line in file:
         for symb in line:
            if symb.isalpha():
                toslt[symb] = toslt.get(symb, 0) + 1
        
    with open(output_path, 'w', encoding='utf-8') as fil:
        for sym, cunt in sorted(toslt.items(), key = lambda item: item[1], reverse=True):
            fil.write(f'{sym} {cunt}\n')

inputi = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 6. «Война и мир»\voina-i-mir\voina-i-mir.txt'
outputi = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 6. «Война и мир»\voina-i-mir\sort.txt'

find_and_find(inputi, outputi)