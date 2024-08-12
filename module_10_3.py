import threading
from random import randint
from  time import sleep
from threading import Thread, Lock

lock1 = threading.Lock()

class Bank:
    def __init__(self, balance: int == 0, lock: Lock == lock1):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            cash = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += cash
            print(f'Пополнение: {cash}. Баланс: {self.balance}')
        sleep(0.001)

    def take(self):
        for i in range(100):
            cash_ = randint(50, 500)
            print(f'Запрос на {cash_}')
            if cash_ <= self.balance:
                self.balance -= cash_
                print(f'Снятие: {cash_}. Баланс: {self.balance}')
            elif cash_ >= self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank(balance=0, lock=lock1)
th1 = Thread(target=Bank.deposit, args=(bk, ))
th2 = Thread(target=Bank.take, args=(bk, ))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')