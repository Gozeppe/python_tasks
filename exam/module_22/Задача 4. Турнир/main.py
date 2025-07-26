import os

def get_score(scor):
    return scor[2]

def find_and_write(input_path, output_path):
    qialified = []
    with open(input_path, 'r', encoding='utf-8') as file:
        K = int(file.readline())
        
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                
              surname, name, score = parts
              score = int(score)
              if score >= int(K):
               initial = name[0] + '.'
               qialified.append((initial, surname, score))
               qialified.sort(key=get_score, reverse=True)
    with open(output_path, 'w', encoding='utf-8') as out_file:
     out_file.write(f"{len(qialified)}\n")  # сначала пишем количество
     for index, (initial, surname, score) in enumerate(qialified, start=1):
        out_file.write(f"{index}) {initial} {surname} {score}\n")

        
        
input_file = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 4. Турнир\first_tour.txt'
output_file = r'D:\Learning\Python\python_tasks\exam\module_22\Задача 4. Турнир\second_tour.txt'
