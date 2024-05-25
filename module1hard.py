grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
s = {}
d = [] #список студентов
d = list(sorted(students))
grades_s = []
for i in range(len(grades)):  #считаем средний бал каждого в новый список
        grades_s.append(sum(grades[i])/len(grades[i]))
s = dict(zip(d, grades_s))#записываем все в словарь
print(s)