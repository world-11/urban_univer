def custom_write(file_name, strings: list):
    strings_positions = {}
    ind = 0
    j: int  #курсор
    file = open(file_name, "a", encoding="utf-8")
    for i in strings:
        ind = strings.index(i) + 1
        j = file.tell()
        file.write(f'{i}\n')
        strings_positions[(ind, j)] = i
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
