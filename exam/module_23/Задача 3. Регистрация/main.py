input_path = r'D:\Learning\Python\python_tasks\exam\module_23\Задача 3. Регистрация\registration.txt'
goods = r'D:\Learning\Python\python_tasks\exam\module_23\Задача 3. Регистрация\registration_good.log'
bad = r'D:\Learning\Python\python_tasks\exam\module_23\Задача 3. Регистрация\registration_bad.log'


def validate_reg(line):
    fields = line.strip().split()
    if len(fields) != 3:
        raise IndexError('НЕ присутствуют все три поля')
    name, email, age = fields
    if not name.isalpha():
        raise NameError('Поле «Имя» содержит не только буквы')
    if '@' not in email or '.' not in email:
        raise SyntaxError('Поле «Имейл» не содержит @ и точку')
    if not age.isdigit() or not 10 <= int(age) <= 99:
        raise ValueError('Поле «Возраст» НЕ представляет число от 10 до 99')


with open(input_path, 'r', encoding='utf-8') as file, \
     open(goods, 'a', encoding='utf-8') as filo, \
     open(bad, 'a', encoding='utf-8') as bad_log:
    for line in file:
        try:
            validate_reg(line)
            filo.write(line)
        except Exception as e:
            # Строка из файла + описание ошибки (без [])
            print(f"{line.strip()}        {e}")
            bad_log.write(f"{line.strip()}\t{e}\n")
