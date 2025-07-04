
# Задача 1. Зоопарк
# В маленьком зоопарке каждое животное сидит в отдельной клетке, всего этих животных четверо: лев, кенгуру, слон и обезьяна. 
# В базе данных они хранятся в виде вот такого списка:

# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Сегодня в зоопарк завезли медведя (bear) и посадили его между львом и кенгуру. В итоге животных стало пять.
#  А через неделю слона перевезли в другое место и в списке снова стало четверо животных.

# Реализуйте эти действия в коде программы и выведите в консоль итоговый список животных, а также покажите, в какой клетке сидят лев и обезьяна. 
# Для этого используйте методы списков.

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

zoo.insert(1, 'bear')
zoo.remove('elephant')
monkey_position = zoo.index('monkey')
lion_position = zoo.index('lion')

print(f'Зоопарк: {zoo},\nЛев сидит в клетке {lion_position + 1},\nОбезьяна сидит в клетке {monkey_position + 1}')

# Результат работы программы:

# Зоопарк: ['lion', 'bear', 'kangaroo', 'monkey']

# Лев сидит в клетке номер 1

# Обезьяна сидит в клетке номер 4


# Задача 2. Сокращения
# В одной компании наступили «тёмные времена», и сотрудников стали сокращать. Зарплаты сотрудников хранятся в списке из N этих самых зарплат. 
# Зарплаты уже уволенных сотрудников обозначаются в списке числом 0.

# Напишите программу, которая запрашивает у пользователя количество сотрудников и их зарплаты,
#  затем удаляет все элементы списка со значением 0 и выводит в консоль, сколько сотрудников осталось, а также их зарплаты.
#  Дополнительный список использовать нельзя.

N = int(input('Введите количество сотрудников: '))
employes = []
for i in range(N):
  paycheck = int(input(f'Введите зарплату {i + 1} сотрудника: '))
  employes.append(paycheck)

employes = [paycheck for paycheck in employes if paycheck != 0]
employes_count = len(employes)

min_paycheck = min(employes)
max_paycheck = max(employes)

print(f'Сотрудников осталось: {employes_count}, \nМаксимальная зарплата: {max_paycheck} \nМинимальная зарплата: {min_paycheck}')
 


# Пример:

# Кол-во сотрудников: 7

# Зарплата 1 сотрудника: 10000

# Зарплата 2 сотрудника: 25000

# Зарплата 3 сотрудника: 0

# Зарплата 4 сотрудника: 50000

# Зарплата 5 сотрудника: 60000

# Зарплата 6 сотрудника: 0

# Зарплата 7 сотрудника: 17000

 

# Осталось сотрудников: 5

# Зарплаты: [10000, 25000, 50000, 60000, 17000]

 

# Дополнительно: выведите на экран максимальную и минимальную зарплату оставшихся сотрудников. Для этого используйте функции max и min. 
# Да, те самые, которыми нельзя называть переменные. В скобках функций просто укажите список.

 

# Пример:

# Максимальная зп: 60000

# Минимальная зп: 10000



# Задача 3. Кино
# Мы поддерживаем свой киносайт и хотим сделать так, чтобы пользователи после регистрации могли создать собственный рейтинг фильмов из тех, 
# которые есть на сайте. Вот сам список фильмов (конечно же, можете брать свои):

 

# films = [

#     'Крепкий орешек', 'Назад в будущее', 'Таксист', 

#     'Леон', 'Богемская рапсодия', 'Город грехов',

#     'Мементо', 'Отступники', 'Деревня', 

#     'Проклятый остров', 'Начало', 'Матрица'

# ]

 

# Напишите программу, которая позволяет добавлять в свой рейтинг фильмы, удалять их оттуда, а также вставлять на нужное пользователю место. Обеспечьте контроль ввода и сделайте так, чтобы в список нельзя было добавить один и тот же фильм несколько раз.

 

# Пример:
# Ваш текущий топ фильмов: []
# Название фильма: Леон
# Команды: добавить, вставить, удалить
# Введите команду: добавить


# Ваш текущий топ фильмов: [‘Леон’]
# Название фильма: Леон
# Команды: добавить, вставить, удалить
# Введите команду: добавить
# Этот фильм уже есть в вашем списке.


# Ваш текущий топ фильмов: [‘Леон’]
# Название фильма: Матрица
# Команды: добавить, вставить, удалить
# Введите команду: добавить


# Ваш текущий топ фильмов: [‘Леон’, ‘Матрица’]
# Название фильма: Леон
# Команды: добавить, вставить, удалить
# Введите команду: удалить


# Ваш текущий топ фильмов: [‘Матрица’]
# Название фильма: …..

user_films = []
while True:

 print(f'Ваш текущий топ фильмов: {user_films}')
 print('добавить, вставить, удалить')
 command = input('Введите команду: ')
 film = input('Название фильма:')

 if command == 'добавить':
    if film in user_films:
        print('Этот фильм уже есть в вашем списке.')
    else:
        user_films.append(film)
        print(f'Фильм "{film}" добавлен в ваш список.')
 elif command == 'вставить':
    index = int(input('На какое место вы хотите вставить фильм? (Введите индекс): '))
    user_films.insert(index - 1, film)
 elif command == 'удалить':
    if film in user_films:
        user_films.remove(film)
        print(f'Фильм "{film}" удалён из вашего списка.')
    else:
        print(f'Фильм "{film}" не найден в вашем списке.')
 elif command == 'выход':
    print("Спасибо за использование нашего приложения. До свидания!")
    break
 else:
    print('Неверная команда, для выхода напишите: выход ')