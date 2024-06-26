#1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(2,3,7)
#print_params(3,2,1,3,45,1,4) ошибка из-за большого количества параметров
print_params(False, 'asd', 12)

print_params(b=25)
print_params(c=[1,2,3])

#2
values_list = [12.7, 'Футбол', False]
values_dict = {'a': 'Дерево', 'b': 'земля', 'c': 'Проба'}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [False, 13]
print_params(*values_list_2, 42)
