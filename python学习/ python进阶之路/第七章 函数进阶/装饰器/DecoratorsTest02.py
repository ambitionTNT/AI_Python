# python learing
# author:TNT
from functools import wraps
from time import time


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time() - start}秒')
        return result
    return wrapper
'''
如果装饰器不希望跟print函数耦合，可以编写可以参数化的装饰器。
'''
"""
    来想想这个问题，难道@wraps不也是个装饰器吗？但是，它接收一个参数，
    就像任何普通的函数能做的那样。那么，为什么我们不也那样做呢？ 这是因为，当你使用@my_decorator语法时，
    你是在应用一个以单个函数作为参数的一个包裹函数。记住，Python里每个东西都是一个对象，而且这包括函数！
    记住了这些，我们可以编写一下能返回一个包裹函数的函数。

"""
def record(output):
    """可以参数化的装饰器"""

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return result

        return wrapper

    return decorate

