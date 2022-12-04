# python learing
# author:TNT
import functools

#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('2022.10.25')


f = now

f()
#函数对象有一个__name__属性（注意：是前后各两个下划线），可以拿到函数的名字：
print(now.__name__)
print(f.__name__)
'''
现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下
'''

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now2():
    print('2022.10.25')
print("----------------------------------")
now2()
"""
把@log放到now()函数的定义处，相当于执行了语句：

now = log(now)
由于log()是一个decorator，返回一个函数，所以，原来的now2()函数仍然存在，只是现在同名的now2变量指向了新的函数，
于是调用now2()将执行新函数，即在log2()函数中返回的wrapper()函数。
wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

"""
'''print("----------------------")
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper()

    return decorator

@log('execute')
def now3():
    print('20159999-3-25')
print("000000000000000000000000000000")
'''

'''
和两层嵌套的decorator相比，3层嵌套的效果是这样的：
now = log('execute')(now)
我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，
它们的__name__已经从原来的'now'变成了'wrapper':
'''
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log("hello world")
def now3():
    print("2022/10/25")
# 定义wrapper()的前面加上@functools.wraps(func)即可。

print("---")
now3()