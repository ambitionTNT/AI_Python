# python learing
# author:TNT


# python中对象有个魔法属性__class__,可以查看对象是由哪个类创建出来的：
print("abc".__class__)
num = 123
print(num.__class__)
# 没错，int、str等数据类型也是一个个的类，
# 具体的字符串和数字其实是他们实例化对象。
class Demo(object):
    pass

demo = Demo()
print(demo.__class__)

print(Demo.__class__)#<class 'type'>
# 这个type其实就是平时我们用来查看数据类型的内建函数：

print(type(num))
# 在只使用这个功能时，作用与__class__相同。
# 而其实type就是一个元类，它还有⼀种完全不同的功能：动态的创建类
print(type("Demo2",(),{}))

class Meta(type):

    def __new__(cls, name, bases, dct):
        print('create class %s' % name)
        return type.__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('Init class %s' % name)
        type.__init__(cls, name, bases, dct)  # 注意__init__方法禁止返回值


class Base(metaclass=Meta):
    pass
'''
一般来说，定义的元类应该重新实现__init__()与__new__()方法
如果需要修改类的属性，使用元类的__new__方法
如果只是做一些类属性检查的工作，使用元类的__init__方法。
'''
print(Base)



'''
事实上，__metaclass__实际上可以被任意调⽤，它只是规定了类“按照什么样的规则去生成”，并不需要是⼀个正式 的类。

比如，我们有一个比较二的需求：你决定在你的模块⾥，所有的类的属性都应该是⼤写形式。
'''


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """遍历属性字典，把不是__开头的属性名字变为⼤写"""
    newAttr = {}
    for name, value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value
    return type(future_class_name, future_class_parents, newAttr)
class Foo(object, metaclass=upper_attr):
    bar = 'bip'


foo = Foo()

'''

print(foo.bar)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Foo' object has no attribute 'bar
'''
print(foo.BAR)




















