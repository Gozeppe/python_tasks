# Задача 1. Задачи компаний
# Одна IT-компания решила расшириться и взяла под своё крыло ещё три таких же, но поменьше. 
# Конечно же, все выполненные и невыполненные задачи этих компаний перетекли в основную компанию.

# Даны четыре списка компаний, в которых для каждой задачи написано, выполнена (1) она или нет (0):

 

# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]

# first_company = [0, 0, 0]

# second_company = [1, 0, 0, 1, 1]

# third_company = [1, 1, 1, 0, 1]

 

# Напишите программу, которая расширяет список main элементами остальных списков, выведите итоговый список, 
# а также выведите количество невыполненных задач.

 

# Результат работы программы:

 

# Общий список задач: [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1]

# Кол-во невыполненных задач: 10



# Задача 2. Вредоносное ПО
# Гера решил попрактиковаться в программировании и захотел написать небольшой скрипт, 
# который после двух сообщений отправляет ещё одно на основе первых двух.

# Пользователь вводит две строки. В каждой из них есть какое-то количество специальных символов ! и ?. 
# Напишите программу, которая считает количество этих символов отдельно в первой строке и отдельно во второй. Если в первой строке их больше,
#  чем во второй, то на экран выводится первая строчка, объединённая со второй, а иначе — вторая с первой.
#  При равном количестве символов в строках выводится «Ой».

 

# Пример 1:

# Первое сообщение: Привет!

# Второе сообщение: Как дела? Что делаешь?

 

# Третье сообщение: Как дела? Что делаешь? Привет!

 

# Пример 2:

# Первое сообщение: Хм!!

# Второе сообщение: ?

 

# Третье сообщение: Хм!!?



# Задача 3. Пакеты
# При работе с сервером мы кодируем сообщение и отправляем его в виде пакетов информации. Их количество равно N. 
# Допустим, каждый пакет содержит четыре числа, каждое из которых равно нулю или единице. Эти числа называются битами.
#  Иногда в кодировке сообщения встречаются ошибки, и в пакете эта ошибка обозначается числом -1. Если таких ошибок не больше одной,
#  то этот пакет мы целиком добавляем в список для декодирования, а иначе отбрасываем.

# Напишите программу, которая будет обрабатывать полученные пакеты и выведет на экран итоговое сообщение для декодирования, 
# а также количество ошибок в нём и количество необработанных пакетов.

 

# Пример:
# Кол-во пакетов: 3


# Пакет номер 1
# 1 бит: 1
# 2 бит: 0
# 3 бит: -1
# 4 бит: 1


# Пакет номер 2
# 1 бит: -1
# 2 бит: -1
# 3 бит: 1
# 4 бит: 1
# Много ошибок в пакете.


# Пакет номер 3
# 1 бит: 0
# 2 бит: 1
# 3 бит: 1
# 4 бит: 1


# Полученное сообщение: [1, 0, -1, 1, 0, 1, 1, 1]
# Кол-во ошибок в сообщении: 1
# Кол-во потерянных пакетов: 1

