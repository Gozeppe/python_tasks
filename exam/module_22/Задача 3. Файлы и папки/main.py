import os

def elem_sum(path):
    sum_of_elems = 0
    dirs_elems = 0
    files_elems = 0

    for root, dirs, files in os.walk(path):
        dirs_elems += len(dirs)
        files_elems += len(files)
        for file in files:
            full_path = os.path.join(root, file)
            try:
                sum_of_elems += os.path.getsize(full_path)
            except FileNotFoundError:
                continue  # если файл исчез — пропускаем
            except PermissionError:
                continue  # если нет прав — тоже пропускаем

    size_in_kb = sum_of_elems / 1024
    return f'Размер: {size_in_kb} КБ\nКаталогов: {dirs_elems}\nФайлов: {files_elems}'

input_path = r'D:\Learning\Python'
print(elem_sum(input_path))