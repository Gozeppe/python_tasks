# 🧩 1. Класс Book
# Создай класс Book, у которого:

# поля: title, author, year;

# метод info(), возвращает строку:
# "Книга: Название (Автор, Год)".


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = int(year)
        
    def info(self):
        return f'Книга: {self.title} ({self.author, self.year})'

book_1 = Book('Исида', 'Как всё обоссать', 2025)
print(book_1.info())
# 🧩 2. Класс User
# У класса User:

# поля: name, age;

# метод greet(), который печатает:
# "Привет, меня зовут [имя] и мне [возраст] лет."


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
    def greet(self):
        print('Привет, меня зовут {0} и мне {1}'.format(self.name, self.age))
        
user_1 = User('Макария', 25)
user_1.greet()
# 🧩 3. Класс Rectangle
# Поля: width, height;
# Метод area(), который возвращает площадь прямоугольника.

class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)        
        self.height = int(height)
        
    def area(self):
        result = self.width * self.height
        return result

triangle_1 = Rectangle(5, 10)
print(triangle_1.area())