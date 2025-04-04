# Задача 1. Заказ
# После того, как человек сделал заказ в интернет-магазине, ему на почту приходит оповещение с его именем и номером заказа.

# Напишите программу, которая получает на вход имя и код заказа, а затем выводит на экран соответствующее сообщение. 
# Для решения используйте строковый метод format.

# Пример:

# Имя: Иван

# Номер заказа: 10948

# Здравствуйте, Иван! Ваш номер заказа: 10948. Приятного дня!

user_name = input('Имя: ')
user_order = int(input('Номер заказа: '))

answer = "Здравстуйте, {name}! Ваш номер заказа: {order}".format(user_name,user_order)
print(answer)

# Задача 2. Долги
# Один наш друг занял у нас определённую сумму денег и всё никак не может их вернуть. А деньги нам нужны. Поэтому мы решили написать небольшой скрипт-напоминалку, который, возможно, разбудит его совесть.

# Напишите программу, которая получает на вход имя и долг, а затем выводит на экран сообщение, где имя повторяется несколько раз (и долг, возможно, тоже). Используйте числа в названиях ключей.

 
# Пример:

# Введите имя: Том

# Введите долг: 100

# Том! Том, привет! Как дела, Том? Где мои 100 рублей? Том! 

user_name = input('Введите имя: ')
user_debt = int(input('Введите долг: '))

sentence = "{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}!".format(user_name, user_debt)
print(sentence)

# Задача 3. IP-адрес
# IP-адрес компьютера состоит из 4 чисел, разделённых точкой. Каждое число находится в диапазоне от 0 до 255 (включительно).

 

# Пример правильного адреса: 192.168.1.0

# Пример неправильного адреса: 192.168.300.0

 

# Напишите программу, которая получает на вход 4 числа и выводит на экран IP-адрес. Используйте переменную ip_address в качестве шаблона.
#  Обеспечьте контроль ввода.

ip_adress = []
for _ in range(4):
    while True:  # Повторяем ввод, пока не получим корректное число
        try:
            ip_num = int(input('Введите число от 0 до 255: '))
            if 0 <= ip_num <= 255:
                ip_adress.append(ip_num)
                break  # Выход из цикла при успешном вводе
            else:
                print('Неверное число, попробуйте снова.')
        except ValueError:
            print('Ошибка! Введите целое число.')

ip_final = "{0}.{1}.{2}.{3}".format(*ip_adress)
print("Ваш IP-адрес:", ip_final)
