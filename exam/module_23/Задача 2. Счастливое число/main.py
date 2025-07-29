import random


out_file = r'D:\Learning\Python\python_tasks\exam\module_23\Задача 2. Счастливое число\out_file.txt'
err_file = r'D:\Learning\Python\python_tasks\exam\module_23\Задача 2. Счастливое число\errors.txt'

total = 777
user_total = 0


def random_fail():
    if random.randint(1, 13) == 7:
        raise RuntimeError("Вас постигла неудача!")
    
while True: 
    
 try:
  user_input = int(input('Введите число: '))
  
  random_fail()
  with open (out_file, 'w', encoding='utf-8') as fil:
          fil.write(str(f'{user_input}\n'))
          user_total += user_input
          if user_total == total:
              print('Удача, ура')
              break
  
 
 except ValueError as e:
     print('Это не число, введи число')
     with open(err_file, 'a', encoding='utf-8') as file:
         file.write(f'{e}')
 except RuntimeError as e:
    print(e) 



