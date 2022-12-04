# python learing
# author:TNT
class Fib(object):

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        # self.c = 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.num:
            # temp = self.c
            # self.c = self.a + self.b
            # self.a = self.b
            # self.b = temp
            self.a, self.b = self.b, self.b + self.a
            self.index +=1
            return self .a

        raise StopIteration()

# 生成器是语法简化版的迭代器。
def fib(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        '''
        相当于：

        t = (b, a + b) # t是一个tuple
        a = t[0]
        b = t[1]
        但不必显式写出临时变量t就可以赋值。

上   面的函数可以输出斐波那契数列的前N个数：
        '''
        yield a


for n in fib(6):
    print(n)
