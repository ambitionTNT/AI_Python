# python learing
# author:TNT
import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor


class Account(object):
    """银行家"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, money):
        # 通过锁保护临界资源
        # 首先要获得锁，进入临界区
        # with语句自带关闭,以及释放
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance

def main():
    """主函数"""
    account = Account()
    #创建线程池
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for _ in range(100):
        # 将函数提交给线程池
        future = pool.submit(account.deposit, 1)
        futures.append(future)
    # 关闭线程池
    pool.shutdown()
    for future in futures:
        future.result()
    print(account.balance)


if __name__ == '__main__':
    main()

