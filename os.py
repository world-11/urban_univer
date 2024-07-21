import os, time

directory = os.getcwd()

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(os.getcwd(), file)
    filetime = os.stat(file).st_mtime
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(os.getcwd())
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:'
          f'{formatted_time}, Родительская директория: {parent_dir}')
