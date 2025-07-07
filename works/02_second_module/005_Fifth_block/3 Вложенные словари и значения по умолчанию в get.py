# Задача 1. Заказ фруктов
# В торговую компанию пришёл заказ:

order = {
    'apple': 2,

    'banana': 3,

    'pear': 1,

    'watermelon': 10,

    'chocolate': 5}

# Ключи — названия товаров, значения — необходимое количество килограммов.

# При помощи метода get и установки значения по умолчанию проверьте, есть ли товар на складе, и получите его цену. Если товара нет, 
# то по умолчанию получите 0. Подсчитайте итоговую выручку компании по имеющимся товарам.

incomes = {

  'apple': 5600.20,

  'orange': 3500.45,

  'banana': 5000.00,

  'bergamot': 3700.56,

  'durian': 5987.23,
  
  'grapefruit': 300.40,
  
  'peach': 10000.50,

  'pear': 1020.00,

  'persimmon': 310.00,

}

total_income = 0

for item, quantity in order.items():
    price = incomes.get(item, 0)
    total_income += price * quantity
    if price == 0:
        print(f'Товара "{item}" нет на складе. Пропускаем.')

print(f'\nИтоговая выручка по имеющимся товарам: {total_income} рублей')

# Ключи — названия товаров, значения — цена за один килограмм.

# Напишите программу, которая суммирует стоимость (цена × количество) всех заказанных товаров, и выведите итоговую сумму в консоль.

# Если искомого товара нет на складе, то по умолчанию получите 0. В этом поможет метод get и установка значения по умолчанию.



# Задача 2. Игроки
# Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет, а также его текущий статус, в котором указано, отдыхает он, 
# тренируется или путешествует:

players_dict = {

   1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},

   2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},

   3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},

   4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},

   5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},

   6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},

   7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},

   8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}

} 


team_a_members = [
    player['name']
    for player in players_dict.values()
    if player['team'] == "A" and player['status'] == 'Rest'
]
team_b_members = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'B' and player['status'] == 'Training'
]
team_c_members = [
    player['name']
    for player in players_dict.values()
    if player['team'] == 'C' and player['status'] == 'Travel'
]
print(team_a_members)
print()
print(team_b_members)
print()
print(team_c_members)
# Напишите программу, которая выводит на экран следующие данные в разных строках:

# Все члены команды А, которые отдыхают.
# Все члены команды B, которые тренируются.
# Все члены команды C, которые путешествуют.