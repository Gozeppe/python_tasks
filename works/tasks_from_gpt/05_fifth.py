# Задание 3. Бесконечный привет
# Пользователь вводит слово. Пока это не стоп, печатай "Привет, смертный!"
while True:
    user_word = input('Введите слово: ')
    if user_word == 'стоп' or user_word == 'Стоп':
        break
    else:
        print('Привет, смертный!')

# Задание 4. Сумма чисел
# Пользователь вводит числа. Если ввёл 0 — заканчиваем и выводим сумму всех введённых чисел.