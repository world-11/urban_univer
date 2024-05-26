first = int(input('Введите число '))
second = int(input('еще одно '))
third = int(input('и еще одно '))
if first == second and first == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else: print('0')