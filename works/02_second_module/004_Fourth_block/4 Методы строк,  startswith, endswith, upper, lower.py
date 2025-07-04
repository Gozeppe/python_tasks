# Задача 1. Шифр Цезаря 2
# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря. Напомним, 
# что в таком способе шифрования каждая буква заменяется на следующую по алфавиту через K позиций по кругу.

# Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования. Не используйте конкатенацию и сделайте так,
# чтобы текст был в одном регистре.

text = input("Введите текст для шифрования: ").lower()
k = int(input("Введите сдвиг: "))

result = ''.join([
    chr((ord(char) - ord('a') + k) % 26 + ord('a')) if char.isalpha() else char
    for char in text
])

print("Зашифрованный текст:", result)


# Задача 2. Путь к файлу
# Все данные сайта лежат в одном проекте. При написании кода, внутри этого проекта часто используются абсолютные пути файлов, которые необходимо проверять.

# Пользователь вводит абсолютный путь к текстовому файлу, а также проверяемые данные: диск и расширение файла. Напишите программу, 
# которая проверяет корректность этого пути.

file_path = input('Введите путь к файлу: ')
file_true_path = input('На каком диске:')
file_extension = input('Требуемое расширение файла: ')

if file_path.startswith(file_true_path.upper() + ":") and file_path.endswith(file_extension):
    print('Путь корректен!')

# Пример:

# Путь к файлу: C:/user/docs/folder/new_file.txt

# На каком диске должен лежать файл: C

# Требуемое расширение файла: .txt

# Путь корректен!



# Задача 3. Удаление части
# На вход в программу подаётся строка, состоящая из заглавных и строчных букв кириллицы. Напишите код, который проверяет, каких букв в строке больше: 
# строчных или заглавных. Если заглавных букв больше, то сделайте все буквы строки заглавными, иначе сделайте всё строчными.

# Подсказка: используйте методы islower() и/или isupper().

user_text = input('Введите строку: ')

upper_text = [letter for letter in user_text if letter.isupper()]
lower_text = [letter for letter in user_text if letter.islower()]

if len(upper_text) > len(lower_text):
    print(user_text.upper()) 
elif len(lower_text) > len(upper_text):
    print(user_text.lower())
else:
    print('Количество нижних и верхних равно')

# Введите строку: ПитоН - этО хорошО

 

# Результат: питон - это хорошо


 

# Пример 2:

# Введите строку: ПиТоН - ЭтО УДоБнО

 

# Результат: ПИТОН - ЭТО УДОБНО