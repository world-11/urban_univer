import math

class Figure:
    sides_count = 0
    filled: bool = True
    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = list(sides)

    def get_color(self):
        return self.__color

    # валидность задания цвета
    def __is_valid_color(self, r:bytes, g:bytes, b:bytes):
        if r >= 0 and r <=255:
            if g >= 0 and g <= 255:
                if b >= 0 and b <= 255:
                    return True
    # установка света
    def set_color(self, r:bytes, g:bytes, b:bytes):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # валидность чисел сторон
    def __is_valid_sides(self, new_sides):
        check = True
        new_sides_ = list(new_sides)
        if len(new_sides_) == len(self.__sides):
            for i in new_sides_:
                if i > 0 and isinstance(i, int):
                    check = True
                else:
                    check = False
                    break
        return check

    def get_sides(self):
        return self.__sides

    def __len(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides) == True:
            if len(new_sides) == self.sides_count:
                self.__sides = list(new_sides)
            else:
                self.__sides = self.__sides



class Circle(Figure):
    sides_count = 1
    __radius = 1
    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if len(sides) == self.sides_count:
            self._Figure__sides = list(sides)
            self.__radius = sides[0] / (2 * math.pi)
        else:
            self._Figure__sides = [1]

    def __len__(self):
        return self._Figure__sides[0]

    # расчет площади круга
    def get_square(self):
            return 2 * math.pi * ((self.__radius) ** 2)


class Triangle(Figure):
    sides_count = 3
    __height = 0
    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if len(sides) == self.sides_count:
            self._Figure__sides = list(sides)
        else:
            self._Figure__sides = [1, 1, 1]

#     расчет высоты треукгольника
    def __height(self):
        p = sum(list(self._Figure__sides)) / 2  # полупериметр
        __height = int(2 * math.sqrt(p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) *
        (p - self._Figure__sides[2])) / max(self.__sides))
        return self.__height

#     расчет площади треугольника
    def get_square(self):
        p = sum(list(self._Figure__sides)) / 2
        return int(math.sqrt(p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2])))



class Cube(Figure):
    sides_count = 12
    i = 0
    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if len(sides) == 1:
            self._Figure__sides.clear()
            for i in range(12):
                self._Figure__sides.append(sides[0])
        else:
            self._Figure__sides = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#     расчет объема куба
    def get_volume(self):
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((100, 200, 124), 15, 31, 18)




# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

#Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)# Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

#Проверка периметра (круга), это и есть длина:
print(len(circle1))

#Проверка объёма (куба):
print(cube1.get_volume())
cube2 = Cube((222, 35, 130), 8)
print(cube2.get_volume())

#Проверка площади круга
print(circle1.get_square())

#Проверка площади треугольника
print(triangle1.get_square())

#Проверка валидности сторон
triangle2 = Triangle((100, 200, 124), 15, 31, 18)#стороны 1
print(triangle2.get_sides())
cube3 = Cube((-3, 35, 130), 11, 16)#стороны 1
print(cube3.get_sides())
circle2 = Circle((200, 200, 100), 10, 13, 45) # #стороны 1
print(circle2.get_sides())

#Проверка установки цвета
cube1.set_color(123, 31, 0)#изменится
print(cube1.get_color())
triangle2.set_color(32, 13, -1)#не изменится
print(triangle2.get_color())
circle1.set_color(256, 12, 100)#не изменится
print(circle1.get_color())

#Проверка на изменение сторон:
cube1.set_sides(5.5, 3)# Не изменится
print(cube1.get_sides())
triangle1.set_sides(12.1, 13, 17)#не изменится
print(triangle1.get_sides())
circle1.set_sides(-5)#не изменится
print(circle1.get_sides())