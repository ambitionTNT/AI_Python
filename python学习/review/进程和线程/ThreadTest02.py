# python learing
# author:TNT
from threading import Lock
from time import sleep




class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        #先获取锁
        self._lock.acquire()
        try:
            #计算存储后余额
            new_balance = self._balance + money
            sleep(0.01)
            #修改账户余额
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance

