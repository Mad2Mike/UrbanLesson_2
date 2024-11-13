import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self):

        print(f"{self.name} на нас напали! \n")
        enemy_count = 100
        battle_day = 0
        while  enemy_count > 0:
            time.sleep(1)
            enemy_count -= self.power
            battle_day += 1
            print(f"{self.name} сражается {battle_day}..., осталось {enemy_count} воинов.")
        print(f"{self.name} одержал победу спустя {battle_day} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
