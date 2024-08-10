from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name: str, power: int):
        super(Knight, self).__init__()
        self.name = name
        self.power = power



    def run(self):
        print(f'{self.name}, на нас напали!')
        vrag = 100
        time_ = 0
        while vrag != 0:
            vrag -= self.power
            time_ += 1
            sleep(1)
            print(f'{self.name} сражается {time_} дней..., осталось {vrag} воинов.')
        print(f'{self.name} одержал победу спустя {time_} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')