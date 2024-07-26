#Задача 1. Координаты

#Мы тестируем 2D-игру, где нужно управлять подводной лодкой. У лодки есть координаты в пространстве — X (икс) и Y (игрек).

#X — это движение вперёд-назад, а Y — вверх-вниз. Соответственно, во время движения лодки меняются и её координаты.

#Во время тестирования игры нам необходимо сравнивать эти координаты и выводить на экран нужное сообщение, в том числе если они равны.

#Вводятся две координаты — X и Y. С помощью трёх последовательных проверок сравните обе координаты и выведите соответствующее сообщение.

#Пример 1:

#Введите икс: 5

#Введите игрек: 6

#X меньше Y
#Пример 2:

#Введите икс: 3

#Введите игрек: 3

#X равен Yv

x = int(input('Enter X: '))
y = int(input('Enter Y: '))

if x < y:
    print('x lesser than y')
if x > y:
    print('x bigger than y') 
else: 
    print('thay are equal')
#Задача 2. Скидки!

#Напишите программу для примера, разобранного в видео. Пользователь покупает курс стоимостью 75 000 рублей. Если денег на счету достаточно, то нужно:

#Списать со счёта деньги.
#Проверить баланс счёта. Если там меньше 5000 рублей, то зачислить на счёт 1000 рублей и вывести сообщение «Сделана скидка».
#Вывести сообщение «Курс успешно приобретён!».
#Иначе (если денег на счету не хватает) вывести «Не хватает денег на счету». Также в конце вывести остаток счёта и сообщение «Хорошего дня!».

#Пример:

#Сколько денег на счету? 78500

#Курс успешно приобретён

#Сделана скидка

#Остаток на счету: 4500

#Хорошего дня!

bank_money = int(input('Enter bank account: '))

course = 75000

if bank_money > course:
    bank_money -= course
    print('You bought course')
    if bank_money < 5000:
        bank_money += 1000
        print('Discount activated,', 'Money left:', bank_money)
else:
    print("You don't have enough money")

    print('Have a good day!')


#Задача 3. Маша пошла за сыром

#Мама дала Маше денег и отправила её в магазин за сыром. А ещё сказала: «Если останутся деньги, то можешь купить себе мороженое. 
# Если денег на сыр не хватит, значит, их маловато — следовательно, и мороженого не будет».

#Сделайте программу, которая получает на вход количество денег. Сыр стоит 60 рублей, мороженое — 20 рублей. 
#Если денег на сыр хватает (больше либо равно), то:

#Выводите сообщение «На сыр денег хватило» и вычитайте стоимость сыра из кошелька.
#Если оставшихся денег хватает на мороженое, то выводите «И на мороженое тоже!». Иначе выводите «Денег маловато».
#Если денег не хватило даже на сыр, то выводите «Денег не хватило даже на сыр!».

money = int(input('Enter money amount: '))

cheese = 60
ice_cream = 20

if money >= cheese:
    money -= money - cheese
    print('You have enough money to buy cheese!')
    if money >= ice_cream:
        money -= money - ice_cream
        print('And for ice_cream too!')
    else:
        print('Not enought money for ice cream...')
else:
    print("You don't have enough money even for cheese...")