import threading
import time

class Knight(threading.Thread):
    def __init__(self,name,power,enemy=100):
        super().__init__(name=name)
        self.name = name
        self.power=power
        self.enemy=enemy


    def run(self):
        print(f' {self.name} на нас напали')
        days=0
        while self.enemy>0:
            time.sleep(1)
            self.enemy -= self.power
            days += 1
            print(f'{self.name} сражается {days} день(дня), осталось {self.enemy} воинов')
        print(f'{self.name} одержал победу спустя {days} дней')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились')