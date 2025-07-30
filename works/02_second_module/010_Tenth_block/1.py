# 2. Класс “Копилка”
# При создании копилка всегда пустая.

# Метод add(self, amount): добавляет монетки.

# Метод break_piggy(self): выводит "Ты разбил копилку! Там было <сумма> рублей" и обнуляет сумму.

# Можно создать несколько копилок с независимыми суммами.

class Kopilka:
    def __init__(self, name, amount = 0):
        self.name = name
        self.amount = amount
    
    
    def add(self, amount):
        self.amount += amount
        print(f'Вы положили {amount} монет, теперь тут {self.amount} монет')
    
    def break_piggy(self):
        print(f'Ха, лох, разбил копилку {self.name}! А в ней было {self.amount} монет, нищебродина. Иди поплачь.')
        self.amount = 0
    def info(self):
        print(f'В копилке {self.name} - {self.amount} монет')

kopilka_1 = Kopilka('Свинья')
kopilka_2 = Kopilka('Петух')
kopilka_1.info()
kopilka_1.add(200)
kopilka_1.info()
kopilka_1.break_piggy()
kopilka_1.info()
kopilka_2.info()
kopilka_2.add(500)
kopilka_2.info()
kopilka_2.break_piggy()
kopilka_2.info()


# 3. Класс “Бот для спама”
# При создании задаётся имя бота и счётчик отправленных сообщений (по умолчанию 0).

# Метод spam(self, count): увеличивает счётчик на count.

# Метод stats(self): выводит "Бот <имя> отправил <n> сообщений".

class Botik:
    
    def __init__(self, name, msg = 0):
        self.name = name
        self.msg = msg
        
    def spam(self, count):
        
        self.msg += count
    
    def status(self):
        print(f'Бот {self.name} отправил {self.msg} сообщений!')

bot_1 = Botik('Хуётик')
bot_2 = Botik('Пиздотик')

bot_1.spam(2)
bot_1.spam(1)
bot_2.spam(5)
bot_1.status()
bot_2.status()


# 4. Класс “Журнал оценок”
# В конструкторе принимается имя ученика.

# Метод add_mark(self, mark): добавляет оценку в список.

# Метод average(self): возвращает средний балл (или 0, если оценок нет).

# Метод info(self): выводит имя и средний балл.

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        if self.marks:
            return sum(self.marks) / len(self.marks)
        else:
            return 0  # Если нет оценок

    def info(self):
        avg = self.average()  # Получаем актуальный средний балл!
        print(f'У {self.name} средний балл {avg:.2f}')  # округлил до двух знаков, чтобы выглядело круто

stud_1 = Student('Хуент')
stud_1.add_mark(5)
stud_1.add_mark(7)
stud_1.add_mark(1)
stud_1.info()
