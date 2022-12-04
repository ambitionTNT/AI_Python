# python learing
# author:TNT
from threading import Thread

from review.进程和线程.ThreadTest02 import Account


class AddMoneyThread(Thread):


    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    #创建100个存款的线程想同一个账户存钱

    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    #等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()

