# Задача 1. Среднее арифметическое
# Программа получает от пользователя два числа — a и b. Реализуйте функцию, которая принимает на вход числа a и b, 
# считает и выводит в консоль среднее арифметическое всех чисел из отрезка [a; b]. Обеспечьте контроль ввода: не забывайте, 
# что а всегда должно быть меньше, чем b.

a = int(input('Введите число : '))
b = int(input('Введите число : '))
n = 0
count = 0

for i in range (a, b + 1):
 n += i
 count += 1

avg = n / count
print(f'Среднее {avg}')
# Пример:

# Введите левую границу: 3

# Введите правую границу: 8

# Среднее: 5.5


# Усложнение: сделайте это без использования циклов.



# Задача 2. Почта 2
# На почте немного поменялись правила: теперь в почтовом извещении нужно указывать фамилию, имя, страну проживания, город, улицу, 
# номер дома и номер квартиры.

# Реализуйте функцию, которая получает все эти данные и выводит на экран. 
# В программе вызовите функцию три раза с разными значениями аргументов.


# Подсказка: семь аргументов.

def print_all_info_hard(surname, name, country, city, street, house, flat):
    print(f"Фамилия: {surname}\n"
          f"Имя: {name}\n"
          f"Страна проживания: {country}\n"
          f"Город: {city}\n"
          f"Улица: {street}\n"
          f"Номер дома: {house}\n"
          f"Номер квартиры: {flat}")


user_surname = input("Введите фамилию: ")
user_name = input("Введите имя: ")
user_street = input("Введите улицу: ")
user_house = input("Введите номер дома: ")

for _ in range(3):
    user_surname = input("Введите фамилию: ")
    user_name = input("Введите имя: ")
    user_country = input("Введите страну проживания: ")
    user_city = input("Введите город: ")
    user_street = input("Введите улицу: ")
    user_house = input("Введите номер дома: ")
    user_flat = input("Введите номер квартиры: ")

    print_all_info_hard(user_surname, user_name, user_country, user_city, user_street, user_house, user_flat)


# Задача 3. GPS-навигатор 2.0
# Нам поручили усовершенствовать GPS-навигатор, добавив в него новую фишку. 
# Теперь пользователь может не только смотреть расстояние от себя до объекта, 
# но и задавать в навигаторе две произвольные точки, после чего на экран ему выводится расстояние между ними.
#  Для этого пользователь вводит четыре действительных числа x1, y1, x2, y2 — это как раз координаты этих двух точек.

# Напишите программу, где у пользователя спрашивается, чего он хочет — найти расстояние от себя до точки или найти 
# расстояние между двумя произвольными точками, после чего запрашиваются необходимые координаты точек и выводится ответ на экран.

def func(x1, x2, y1, y2):
   if want == 1:
     x3 = x1 - x2
     y3 = y1 - y2
     print(f'Расстояние между точками: {x3}{y3}')
   elif want == 2:
      x_user = input('Введите точку нахождения себя, по оси X: ')
      y_user = input('Введите точку нахождения себя по оси Y: ')
      x4 = x1 - x_user 
      y4 = y1 - y_user
      print(f'Расстояние до точки: {x4}, {y4}')

want = input('Выберите вариант, чего вы хотите,  1/2: ')
x1 = int(input('Введите координаты: '))
x2 = int(input('Введите координаты: '))
y1 = int(input('Введите координаты: '))
y2 = int(input('Введите координаты: '))

func(x1, x2, y1, y2)