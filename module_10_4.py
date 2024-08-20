from queue import Queue
from time import sleep
import threading
from random import randint

class Guest(threading.Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

class Table():
    def __init__(self, number: int, guest: Guest = None):
        self.number = number
        self.guest = None

    def run(self):
        time_ = randint(3, 10)
        sleep(time_)

class Cafe():
    def __init__(self, *tables: Table):
        self.tables = list(tables)
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            table_assigned = False
            for table in tables:
                if table.guest == None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table_assigned = True
                    break
            if not table_assigned:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                if not self.queue.empty() and table.guest is None:
                    guest_from_queue = self.queue.get()
                    table.guest = guest_from_queue
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    guest_from_queue.start()




# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()