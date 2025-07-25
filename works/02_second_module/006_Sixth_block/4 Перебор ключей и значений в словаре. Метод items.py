# Задача 1. Кризис миновал
# Закупки грейпфрутов прекратились, и кризис в торговой компании закончился. И теперь можно вернуться к обыденным делам. Однако внезапно вы обнаружили, 
# что старый скрипт, который выводит данные о фруктах, куда-то потерялся. Необходимо его восстановить.

# Дан словарь с парами «название фрукта — цена»:

incomes = {

     'apple': 5600.20,

     'orange': 3500.45,

     'banana': 5000.00,

     'bergamot': 3700.56,

     'durian': 5987.23,

     'peach': 10000.50,

     'pear': 1020.00,

     'persimmon': 310.00,

}

for a, b in incomes.items():
    print(a, ' - - ', b)

# Вывести на экран словарь в следующем виде:

# apple -- 5600.2

# orange -- 3500.45

# banana -- 5000.0

# bergamot -- 3700.56

# durian -- 5987.23

# peach -- 10000.5

# pear -- 1020.0

# persimmon -- 310.0

 

# Не используйте обращение по ключу словаря.



# Задача 2. Сервер
# У вас есть данные о сервере, которые хранятся в виде вот такого словаря:

server_data = {

     "server": {

         "host": "127.0.0.1",

         "port": "10"

     },

     "configuration": {

         "access": "true",

         "login": "Ivan",

         "password": "qwerty"

     }

 }

for section, selection_data in server_data.items():
    print(f'{section}:')
    for key, value in selection_data.items():
        print(f'    {key}: {value}')


# Напишите программу, которая выводит для пользователя эти данные так же красиво и понятно, как они представлены в словаре.

# Результат работы программы:

# server:

#     host: 127.0.0.1

#     port: 10

# configuration:

#     access: true

#     login: Ivan

#     password: qwerty



# Задача 3. В одну строчку
# Нашему другу дали задачу: «Есть словарь, в котором ключи — это числа от 0 до 4, а значения ключей — числа 0, 100, 144, 20 и 19 соответственно. 
# Нужно написать программу, которая выводит список тех значений, у которых ключ делится на 2. Причём программа должна быть в одну строчку.» 
# Программа у друга работает, но её не приняли, так как в ней не используется правило «не повторяйся» — это когда части кода не повторяются. 
# Помогите другу исправить решение задачи так, чтобы код в строчке не повторялся. 

 

# Решение друга:

# print([{0: 0, 1: 100, 2: 144, 3: 20, 4: 19}[i_key] for i_key in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19} if i_key % 2 == 0])

print([i_value for i_key, i_value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])