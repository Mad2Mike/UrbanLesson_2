import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.deposit_alive = True


    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)

            self.balance += amount
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {amount}. Баланс: {self.balance}')

            time.sleep(0.001)
        self.lock.release()
        self.deposit_alive = False
        print(self.deposit_alive)


    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            if amount <= self.balance:
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}')
            else:
                if self.deposit_alive:
                    print('Запрос отклонён, недостаточно средств')
                    self.lock.acquire()
                else:
                    print('Запрос отклонён, недостаточно средств')


# Создаем объект класса Bank
bk = Bank()

# Создаем потоки для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ждем завершения потоков
th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}')