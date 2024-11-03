import itertools
import string

def brute_force_password():
    # Читаем пароль из файла
    with open('password.txt', 'r') as file:
        password = file.read().strip()

    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    
    # Перебор всех возможных комбинаций пароля
    for length in range(1, 9):  # Задаём максимальную длину пароля, здесь 8
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            print(f'Попытка {attempts}: {guess}')  # Вывод номера попытки и текущей комбинации

            if guess == password:
                print(f'Пароль найден: {guess} на попытке {attempts}')
                return

    print('Пароль не найден.')

# Запуск функции
brute_force_password()
