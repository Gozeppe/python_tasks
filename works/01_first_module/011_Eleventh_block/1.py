def get_maximum_of_two(first_number, second_number):
    """Возвращает максимум из двух чисел."""
    if first_number > second_number:
        return first_number
    else:
        return second_number

def get_maximum_of_three(first_number, second_number, third_number):
    """Возвращает максимум из трех чисел, используя get_maximum_of_two."""
    max_of_first_two = get_maximum_of_two(first_number, second_number)
    if max_of_first_two > third_number:
        return max_of_first_two
    else:
        return third_number

# Ввод чисел от пользователя
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
number3 = float(input("Введите третье число: "))

# Нахождение максимума и вывод результата
maximum_value = get_maximum_of_three(number1, number2, number3)
print(f"Максимальное число: {maximum_value}")