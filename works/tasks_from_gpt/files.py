import os
import shutil
# 📂 Блок 2: Работа с файлами
# 🧩 4. Сумма чисел из файла
# Файл numbers.txt — по числу на строке.
# Прочитай все числа, посчитай сумму, запиши её в result.txt.

fil_path = r'D:\Learning\Python\python_tasks\works\tasks_from_gpt\numbers.txt'
filli_path = r'D:\Learning\Python\python_tasks\works\tasks_from_gpt\result.txt'
file_path = r'D:\Learning\Python\python_tasks\works\tasks_from_gpt\words.txt'
filee_path = r'D:\Learning\Python\python_tasks\works\tasks_from_gpt\filtered.txt'
copy_path = r'D:\Learning\Python\python_tasks\works\tasks_from_gpt\copy.txt'
result = 0
with open(fil_path, 'r', encoding='utf-8') as file: 
    for line in file: 
        for num in line.strip(): num = int(num) 
        result += num 
with open (filli_path, 'w', encoding='utf-8') as filli:
    filli.write(str(result))
 




# 🧩 5. Фильтр по длине
# Файл words.txt, каждое слово на новой строке.
# Скопируй в filtered.txt только слова длиной больше 5 символов.
listord = []

with open(file_path, 'r', encoding='utf-8') as filee:
   for strink in filee:          # читаем строку из файла
    for word in strink.split():  # делим строку на слова (по пробелам)
        clean_word = word.strip()  # убираем пробелы, табы, \\n вокруг
        if len(clean_word) >= 5:   # проверка длины слова
            listord.append(clean_word)  # добавляем в список

with open(filee_path, "w", encoding="utf-8") as f:
    for word in listord:
        f.write(word + "\n")

# 🧩 6. Копия файла
# Сделай копию файла original.txt, назвав его copy.txt.



shutil.copy(fil_path, copy_path)