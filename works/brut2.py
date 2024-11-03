import itertools
import string

def brute_force_password():
    # Читаем пароль из файла
    with open('C:/learning/python/python_tasks/works/password.txt', 'r') as file:
        password = file.read().strip()

    characters = string.ascii_letters + string.digits  # Используем буквы и цифры
    found_password = ''  # Здесь будем собирать найденный пароль
    attempts = 0
    
    # Поиск каждого символа пароля по порядку
    for i in range(len(password)):
        for guess in characters:
            attempts += 1
            print(f'Попытка {attempts}: {found_password + guess}')  # Вывод текущего состояния пароля

            if guess == password[i]:
                found_password += guess
                print(f'Найден символ {i+1}: {guess}')
                break  # Переходим к следующему символу

    print(f'Пароль полностью найден: {found_password}')

# Запуск функции
brute_force_password()
