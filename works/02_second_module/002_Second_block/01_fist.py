
# Задача 1. Зоопарк
# В маленьком зоопарке каждое животное сидит в отдельной клетке, всего этих животных четверо: лев, кенгуру, слон и обезьяна. 
# В базе данных они хранятся в виде вот такого списка:

# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Сегодня в зоопарк завезли медведя (bear) и посадили его между львом и кенгуру. В итоге животных стало пять.
#  А через неделю слона перевезли в другое место и в списке снова стало четверо животных.

# Реализуйте эти действия в коде программы и выведите в консоль итоговый список животных, а также покажите, в какой клетке сидят лев и обезьяна. 
# Для этого используйте методы списков.

 

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
# Мы поддерживаем свой киносайт и хотим сделать так, чтобы пользователи после регистрации могли создать собственный рейтинг фильмов из тех, которые есть на сайте. Вот сам список фильмов (конечно же, можете брать свои):

 

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

