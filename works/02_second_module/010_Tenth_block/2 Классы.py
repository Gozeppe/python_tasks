# Задача 1. Машина
# Напишите класс Toyota, состоящий из четырёх статических атрибутов: 

# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.


import random

class Toyota:
    color = 'red'
    price = '1000000'
    max_speed = '200'
    current_speed = '0'

toyota_1 = Toyota()
toyota_2 = Toyota()
toyota_3 = Toyota()
toyota_1.current_speed = random.randint(0, 200)
toyota_2.current_speed = random.randint(0, 200)
toyota_3.current_speed = random.randint(0, 200) 


cars = [toyota_1, toyota_2, toyota_3]
for i, car in enumerate(cars, 1):
    print(f'Car {i}: Цвет: {car.color}, Цена: {car.price}, Макс. скорость: {car.max_speed}, Текущая скорость: {car.current_speed}')

# Задача 2. Однотипные объекты
# В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора есть четыре характеристики: название производителя, матрица, разрешение и частота обновления экрана. Все четыре монитора отличаются только частотой.

# У наушников три характеристики: название производителя, чувствительность и наличие микрофона. Отличие только в наличии микрофона.

 

# Для внесения в базу программист начал писать такой код:

# monitor_name_1 = 'Samsung'

# monitor_matrix_1 = 'VA'

# monitor_res_1 = 'WQHD'

# monitor_freq_1 = 60

# monitor_name_2 = 'Samsung'

# monitor_matrix_2 = 'VA'

# monitor_res_2 = 'WQHD'

# monitor_freq_2 = 144

# monitor_name_3 = 'Samsung'

# monitor_matrix_3 = 'VA'

# monitor_res_3 = 'WQHD'

# monitor_freq_3 = 70

# monitor_name_4 = 'Samsung'

# monitor_matrix_4 = 'VA'

# monitor_res_4 = 'WQHD'

# monitor_freq_4 = 60

 

# headphones_name_1 = 'Sony'

# headphones_sensitivity_1 = 108

# headphones_micro_1 = False

# headphones_name_2 = 'Sony'

# headphones_sensitivity_2 = 108

# headphones_micro_2 = True

# headphones_name_3 = 'Sony'

# headphones_sensitivity_3 = 108

# headphones_micro_3 = True

 

# Поправьте программиста: перепишите код, используя классы и экземпляры классов.

class Monitor:
    name = 'name'
    matrix = 'matrix'
    res = 'res'
    freq = 0
    
class Headphones:
    name = 'name'
    sensitivity = 0
    micro = bool

monitor_1 = Monitor()
monitor_2 = Monitor()
monitor_3 = Monitor()
monitor_4 = Monitor()

headphones_1 = Headphones()
headphones_2 = Headphones()
headphones_3 = Headphones()


monitor_1.name = 'Samsung'

monitor_1.matrix = 'VA'

monitor_1.res = 'WQHD'

monitor_1.freq = 60



monitor_2.name = 'Samsung'

monitor_2.matrix = 'VA'

monitor_2.res = 'WQHD'

monitor_2.freq = 144



monitor_3.name = 'Samsung'

monitor_3.matrix = 'VA'

monitor_3.res = 'WQHD'

monitor_3.freq = 70



monitor_4.name = 'Samsung'

monitor_4.matrix = 'VA'

monitor_4.res = 'WQHD'

monitor_4.freq = 60

 

headphones_1.name = 'Sony'

headphones_1.sensitivity = 108

headphones_1.micro = False



headphones_2.name = 'Sony'

headphones_2.sensitivity = 108

headphones_2.micro = True



headphones_3.name = 'Sony'

headphones_3.sensitivity = 108

headphones_3.micro = True

monitor = [monitor_1, monitor_2, monitor_3, monitor_4]
for i, monitor in enumerate(monitor, 1):
    print(f'Monitor {i}: Название: {monitor.name}, Матрица: {monitor.matrix}, Разрешение: {monitor.res}, Частота: {monitor.freq}\n')
    
    
headphones = [headphones_1, headphones_2, headphones_3]
for i, headphones in enumerate(headphones, 1):
    print(f'\nHeadphones {i}: Название: {headphones.name}, Чувствительность: {headphones.sensitivity}, Микрофон: {headphones.micro}\n')

