# python learing
# author:TNT
"""
特殊的属性和方法
使用__的属性
__dict__:查看对象属性的字典
__class__:查看所属类
__bases__:查看父类
__base__ :查看第一个继承的父类
__mro__ :查看层次结构
__subclasses__()子类的列表




使用__的方法__
__len__:输出长度
__add__:重载
__new__:用于创建对象
__init__:对创建的对象进行初始化

























"""
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name):
        self.name=name

x=C('Jack')
print(x.__dict__)#实例对象的属性字典
print(C.__dict__)
print('-------------------------------')
print(x.__class__)
print(C.__bases__)
print(C.__base__)



a=20
b=100
c=a+b
print(c)
print(b)
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self,other):
        return self.name+other.name

stu1=Student('张三')
stu2=Student('李四')
s=stu1+stu2
print(s)


class Person(object):
    def __init__(self,name,age):
        self.name=name
        self,age=age
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了,cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id:{0}'.format(id(obj)))
        return  obj

    def __init__(self,name,age):
        print('__init__被调用了,self的id值为:{0}'.format(id(self)))
        self.name=name
        self.age=age





