# python learing
# author:TNT



# 我们可以通过调用实例属性的方式来访问：




# 然后我们定义一个 Mixin 类：

class MappingMixin:
    def __getitem__(self, key):
        return self.__dict__.get(key)
    def __setitem__(self, key, value):
        return self.__dict__.set(key, value)

'''这个类可以让子类拥有像 dict 一样调用属性的功能

我们将这个 Mixin 加入到 Person 类中：'''
class Person(MappingMixin):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

p = Person("小陈", "男", 19)
print(p['name'])


# 再定义一个 Mixin 类，这个类实现了 __repr__ 方法，能自动将属性与值拼接成字符串：
class Reprmixin:

    def __repr__(self):
        s = self.__class__.__name__ + '('
        for k, v in self.__dict__.items():
            if not k.startswith('_'):
                s += '{}={}, '.format(k, v)
        s = s.rstrip(', ') + ')'  # 将最后一个逗号和空格换成括号
        return s
# 利用 Python 的特性，一个类可以继承多个父类：

class Person2(MappingMixin, Reprmixin):

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

p = Person2("小陈", "男", 18)
print(p['name'])  # "小陈"
print(p)  # Person(name=小陈, gender=男, age=18)