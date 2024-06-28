class Buiding:
    total = 1
    def __init__(self, name):
        self.name = name
        Buiding.total += 1

blocks = {}
for i in range(40):
    blocks[i] = Buiding(f'Строение_{Buiding.total}')
    print(blocks[i].name, type(blocks[i]))
