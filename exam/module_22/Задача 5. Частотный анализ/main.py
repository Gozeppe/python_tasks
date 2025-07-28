# берём файл тхт, сначала задаём алфавит (a-z), наверняка для этого есть библиотека
# открываем файл, идём по тексту, а! Создаём словарь! Если буква встречается - добавляем её как ключ
# если уже есть, просто увеличиваем, получаем, типо,

# а 2

# м 4

# потом каждое значение через items, вероято, делим на количество букв в тексте. 
# И ещё важно, чтобы он считал только букв, без пробелов и символов

import string

alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

def find_and_count(input_path, output_path):
    dic_count = {}
    total_letters = 0

    with open(input_path, 'r', encoding='utf-8') as inp_file:
        for line in inp_file:
            for symbol in line.lower():  # сразу в нижний регистр
                if symbol in alphabet:   # оставляем только англ. буквы
                    dic_count[symbol] = dic_count.get(symbol, 0) + 1
                    total_letters += 1
        result = []
    for letter, cnt in dic_count.items():
        freq = round(cnt / total_letters, 3)
        result.append((letter, freq))

    result.sort(key=lambda x: (-x[1], x[0]))  # по убыванию доли, потом по алфавиту

    with open(output_path, 'w', encoding='utf-8') as f:
        for letter, freq in result:
            f.write(f"{letter} {freq:.3f}\n")



inputi = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 5. Частотный анализ\text.txt'
outputi = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 5. Частотный анализ\analysis.txt'

find_and_count(inputi, outputi)
