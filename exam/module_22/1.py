import os
import re

def split_tasks_from_text(text):
    pattern = r'(Задача\s+\d+\.\s+[^\n]+)'
    matches = list(re.finditer(pattern, text))

    tasks = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)

        title = match.group(1).strip()
        content = text[start:end].strip()
        tasks.append((title, content))

    return tasks

def sanitize_folder_name(name):
    return re.sub(r'[<>:"/\\|?*]', '', name)

def create_task_folders(base_path, tasks):
    for title, content in tasks:
        folder_name = sanitize_folder_name(title)
        folder_path = os.path.join(base_path, folder_name)

        os.makedirs(folder_path, exist_ok=True)

        main_py_path = os.path.join(folder_path, 'main.py')
        readme_path = os.path.join(folder_path, 'readme.md')

        with open(main_py_path, 'w', encoding='utf-8') as f:
            pass  # Пустой main.py

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_txt_path = os.path.join(script_dir, '1.txt')

    if not os.path.exists(input_txt_path):
        print("Файл 1.txt не найден.")
        return

    with open(input_txt_path, 'r', encoding='utf-8') as f:
        full_text = f.read()

    tasks = split_tasks_from_text(full_text)
    if not tasks:
        print("Не найдено ни одной задачи.")
        return

    create_task_folders(script_dir, tasks)
    print(f"Создано {len(tasks)} задач.")

if __name__ == '__main__':
    main()
