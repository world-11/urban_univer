def add_everything_up(a, b):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    try:
        return round((a + b), 3)
    except TypeError:
        return str(a)+str(b)

    # try:
    #     return a == b
    # except AssertionError:
    #     print("разные значения")

    # try:
    #     print(float(a+b))
    # except ValueError:
    #     print("Нельзя преобразовать во float")



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

