# python learing
# author:TNT
from functools import wraps
from time import time

class Record():
    """通过定义类的方式定义装饰器"""


    def __init__(self, output):
        self.output = output

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args,**kwargs):
            start = time()
            result = func(*args, **kwargs)
'''明：由于对带装饰功能的函数添加了@wraps装饰器，可以通过func.__wrapped__方式获得被装饰之前的函数或类来取消装饰器的作用。'''