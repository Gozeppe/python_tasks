# Задача 1. Машина 2
# Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:

# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
 

# Добавьте два метода класса:

# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Проверьте работу этих методов.

import random

class Toyota:
    color = 'red'
    price = '1000000'
    max_speed = '200'
    current_speed = '0'
    
    def print_info(self):
     print(
        f"Color: {self.color}\n"
        f"Price: {self.price}\n"
        f"Max_speed: {self.max_speed}\n"
        f"Current_speed: {self.current_speed}\n"
    )
    
    def cur_speed(self, current_speed):
        self.current_speed = current_speed
        
        



toyota_1 = Toyota()

toyota_1.print_info()

user_input = int(input('Введите скорость машины: '))

toyota_1.cur_speed(user_input)
toyota_1.print_info()

# Задача 2. Семья
# Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома» и объекты которого могут выполнять следующие действия:

# Отобразить информацию о себе.
# Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»). Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.

 

# Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):

# Family name: Common family

# Family funds: 100000

# Having a house: False

 

# Try to buy a house

# Not enough money!

 

# Earned 800000 money! Current value: 900000

# Try to buy a house again

# House purchased! Current money: 0.0

 

# Family name: Common family

# Family funds: 0.0

# Having a house: True

# Задача 2. Семья
# Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома» и объекты которого могут выполнять следующие действия:

# Отобразить информацию о себе.
# Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»). Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.

 
class Family:
    family_name = 'Хуевы'
    family_funds = 0
    having_a_house = False

    def print_info(self):
        print(
            f'Фамилия: {self.family_name}'
            f'\nСредства: {self.family_funds}'
            f'\nНаличие дома: {self.having_a_house}'
        )

    def earn_money(self, amount):
        self.family_funds += amount
        print(f'Общая сумма сейчас: {self.family_funds}')

    def buy_house(self):
        price = 200000
        print(f'Цена за дом: {price}')
        if self.family_funds >= price:
            self.having_a_house = True
            self.family_funds -= price
            print('Вы купили дом!')
        else:
            print('Надо ещё накопить...')

family = Family()

while True:
    print("\n1 — Показать информацию о семье")
    print("2 — Заработать денег")
    print("3 — Купить дом")
    print("4 — Выйти")
    choice = input("Выбери действие: ")
    
    if choice == "1":
        family.print_info()
    elif choice == "2":
        amount = int(input("Сколько денег заработать? "))
        family.earn_money(amount)
    elif choice == "3":
        family.buy_house()
    elif choice == "4":
        print("Выход.")
        break
    else:
        print("Неизвестная команда!")
    
    
    if family.having_a_house:
        print("Поздравляем! Вы купили дом! Программа завершена.")
        break
