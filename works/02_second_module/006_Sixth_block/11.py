# 1. Списки (list)
# Что это: изменяемая последовательность элементов.

# Основные методы: append, remove, insert, pop, index, срезы ([:]), in.

# Упражнения:
# Создай список из 5 любых чисел. Добавь в конец ещё одно число.

# Удали второй элемент. Замени последний на строку 'конец'.

# Выведи все элементы, кроме первого и последнего.

import random

rand_list = [random.randint(0, 50) for _ in range(5)]
print(rand_list)

1.
rand_list.append(random.randint(0, 50))
print(rand_list)
2.
rand_list.pop(1)
rand_list[-1::] = ['конец']
print(rand_list)
3
rand_slices = rand_list[1:4]
print(rand_slices)
3.

#  2. Кортежи (tuple)
# Что это: неизменяемая версия списка.

# Особенности: чаще используется для хранения "связанных данных", например координат или (имя, возраст).

# Упражнения:
# Создай кортеж с тремя строками.

# Распакуй кортеж в три переменные.

# Преврати кортеж в список, добавь туда новый элемент, снова преврати в кортеж.


words = ['хуй', 'пизда', 'джигурда', 'сепулька', 'ад', 'нозиум', 'Исида', 'Писида']

random_words = random.sample(words, 3)  # Берём 3 разных случайных слова

words_tup = tuple(random_words)

print(words_tup)

a, b, c = words_tup
print(a, b, c)

my_lst = list(words_tup)

my_lst.append(random.choice(words))
print(my_lst)   

new_tup = tuple(my_lst)
print(new_tup)



# 🔹 3. Словари (dict)
# Что это: коллекция пар ключ: значение.

# Основные методы: .get(), .items(), .keys(), .values(), in, доступ по dict['ключ'].

# Упражнения:
# Создай словарь с именами и возрастами.

# Добавь ещё одну пару.

# Удали одного человека.

# Получи список всех имён (ключей).

# Получи средний возраст.
1.

dic_people = {
    'Игорь': '30',
    'Маша': '40',
    'Шпигорь': '99',
    'Хуяша': '666'
}
2.
dic_people.update({'Аркадий': '120',
                    'Мадий' : '300'})
print(dic_people)
3.
del dic_people['Хуяша']
print(dic_people)
4.
find_key = dic_people.keys()
print(find_key)
5.

sum_age = 0
for age in dic_people.values():
    sum_age += int(age)

lenght_dic = len(dic_people)
med_age = sum_age / lenght_dic

print(med_age)




# 🔹 4. Множества (set)
# Что это: неупорядоченная коллекция уникальных элементов.

# Основные операции: .add(), .remove(), in, set(), объединение (|), пересечение (&), разность (-).

# Упражнения:
# Преврати список с дубликатами в множество.

# Удали один элемент.

# Проверь, есть ли 'кот' во множестве.

# Объедини два множества.

import random
unique_part = [random.randint(1, 10) for _ in range(5)]
duplicates = [random.choice(unique_part) for _ in range(3)]
combined = unique_part + duplicates

random.shuffle(combined)
combuned = set(combined)
print(combuned)

# Упражнения:
# Преврати список с дубликатами в множество.

# Удали один элемент.

# Проверь, есть ли 'кот' во множестве.

# Объедини два множества.
1.
new_st = set(combuned)
print(new_st)
2.
random_element = random.choice(list(new_st))

# Удаляем этот элемент
new_st.remove(random_element)
print(new_st)
3. 
print('cat' in new_st)
4.
unique_part_2 = [random.randint(1, 10) for _ in range(5)]
duplicates_2 = [random.choice(unique_part_2) for _ in range(3)]
combined_2 = unique_part_2 + duplicates_2
random.shuffle(combined_2)
combuned_2 = set(combined_2)
print(combuned_2)

combuned_3 = combuned_2.union(combuned)
print(combuned_3)