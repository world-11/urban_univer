class Horse:
    def __init__(self, x_distance: int = 0, sound: str = 'Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        x_distance += dx

class Eagle:
    def __init__ (self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__ (self, x_distance, y_distance, sound):
        super().__init__(x_distance, y_distance, sound)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return print(self.x_distance, self.y_distance)

    def voice(self):
        print(sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()