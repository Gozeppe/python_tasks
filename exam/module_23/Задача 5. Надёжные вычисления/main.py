def sqrt_with_abuse(user_input):
    import math
    try:
        num = int(user_input)
    except ValueError:
        print("Позор! Введи ЧИСЛО, а не свою чушь, абоминейшн!")
        return

    if num < 0:
        print("Слабоумное животное, отрицательное число не бывает инвестицией!")
        return

    try:
        result = math.sqrt(num)
        print(f'Квадратный корень из числа {num} равен {result}')
    except Exception as exc:
        print(f'Произошла невероятная хрень: {exc}')


usr_inp = input('Введите число: ')
 
sqrt_with_abuse(usr_inp)