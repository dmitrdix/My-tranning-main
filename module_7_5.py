import os
import time
#d=r'D:\Дима\Python project\Домашние задания\modul7\test7.txt'
for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(file)))
        parent_dir = os.path.dirname(BASE_DIR)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
              f' Время изменения{formatted_time}: , Родительская директория {parent_dir}:')