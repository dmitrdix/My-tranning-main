import threading
import time
import random

class Bank():
    def __init__(self):
        self.balance=0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(1,100):
            random_integer = random.randint(50,500)
            self.balance=self.balance+random_integer

            if self.balance>=500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение {random_integer}.Баланс:{self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(1,100):
            random_integer = random.randint(50,500)
            print(f'Запрос на {random_integer}')
            if random_integer <=self.balance:
                self.balance -= random_integer
                print(f'Снятие:{random_integer}  Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')