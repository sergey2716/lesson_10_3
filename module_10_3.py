"""
Задача "Банковские операции":
Необходимо создать класс Bank со следующими свойствами:

Атрибуты объекта:
balance - баланс банка (int)
lock - объект класса Lock для блокировки потоков.

Методы объекта:
Метод deposit:
Будет совершать 100 транзакций пополнения средств.
Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
Метод take:
Будет совершать 100 транзакций снятия.
Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
В начале должно выводится сообщение "Запрос на <случайное число>".
Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и заблокировать поток методом acquire.
Далее создайте объект класса Bank и создайте 2 потока для его методов deposit и take. Запустите эти потоки.
После конца работы потоков выведите строку: "Итоговый баланс: <баланс объекта Bank>".

По итогу вы получите скрипт разблокирующий поток до баланса равному 500 и больше или блокирующий, когда происходит попытка снятия при недостаточном балансе.
Пример результата выполнения программы:
Исходный код:
class Bank:
def __init__(self):
....
def deposit(self):
...
def take(self):
...

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
"""
import threading
import time
import random


class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in  range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            random_int = random.randint(50,500)
            self.balance +=random_int
            print(f'Пополнение: {random_int}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            random_int = random.randint(50,500)
            print(f'Запрос на {random_int}')
            if random_int <= self.balance:
                self.balance -= random_int
                print(f'Снятие: {random_int}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                time.sleep(0.001)

bk = Bank()
thr1 = threading.Thread(target=Bank.deposit,args=(bk,))
thr2 = threading.Thread(target=Bank.take,args=(bk,))

thr1.start()
thr2.start()
thr1.join()
thr2.join()

print(f'Итоговый баланс: {bk.balance}')

































