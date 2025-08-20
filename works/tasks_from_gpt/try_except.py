
# ⚠️ Блок 3: Try / Except / Raise
# 🧩 7. Деление
# Функция divide(a, b) делит a на b.
# Если b == 0 — выводит: "Ошибка: деление на ноль".

def divide(a, b):
    try:
     return a / b
    except ZeroDivisionError:
        print('Ошибка деления на ноль!')
        
print(divide(2, 3))
# 🧩 8. Проверка ввода
# Запроси ввод у пользователя.
# Если он ввёл не число — выведи: "Это не число!".

try:
    user_input = int(input('Введите число: '))
except ValueError:
    print('Число, а не слово, наркоман')

# 🧩 9. Открытие файла
# Попроси путь до файла.
# Если файла нет — выведи: "Файл не найден.", не падай.

try:
    user_path = input("Введите путь до файла: ")
    with open(user_path, "r", encoding="utf-8") as f:
        content = f.read()
        print("Файл успешно открыт!")
except FileNotFoundError:
    print("Файл не найден.")
