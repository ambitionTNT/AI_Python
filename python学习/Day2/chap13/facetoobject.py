# python learing
# author:TNT
"""
封装：提高安全度
将数据方法包装到类对象中，在方法内部对属性进行操作，在类对象的外部调用方法。这样，无需关心方法内部的具体实现细节，从而隔离了复杂度
在python中么没有专门的修饰符用于属性的私有，如果该属性不希望在对象外部被访问，前面使用两个__

继承：提高代码的复用性
如果一个类没有继承任何类，则默认继承object
python支持多继承
定义子类是，必须在其构造函数中调用父类的构造函数
class 子类类名（父类1,父类2,。。。）
方法重写:


object类:
object类是所以类的父类，因此所有类都要object类的属性和方法
内置函数dir()可以查看指定对象所有属性

object有一个__str————()方法,用于返回对于“对象的描述”，对应于内置函数str（）经常用于print（）方法，帮助我们查看对象的信息
所有我们常对__str__()进行重写



多态：提高程序的可扩展性和可维护性
简单的说：多态就是具有多种形态，它指的是：即便不知道一个变量所引用的对象到低是什么类型，
仍然可以通过这个变量调用方法，在运行过程中跟据变量所引用的对象的类型，动态的决定调用哪个对象的方法

静态语言&动态语言
静态语言实现多态三个必要条件：
    继承
    方法重写
    父类引用指向子类对象
动态语言的多态崇尚“鸭子类型”当看到一只鸟走起路像鸭子‘游泳起来像鸭子、收起来也像鸭子，那么这只鸟就可以被称为鸭子。
在鸭子类型中，不需要关系对象是什么类型，到低是不是鸭子，只关心对象的行为

"""
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动')


car=Car('宝驴')
car.start()
print(car.brand)
'''

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#age不希望在类的外部被使用，所以加了俩个__
    def show(self):
        print(self.__age,self.name)

stu=Student('z',29)
stu.show()
print(stu.name)
#print(dir(stu))
print(stu._Student__age)
'''

print('---------------------继承-----------------')

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print('姓名{0},年龄{1}'.format(self.name,self.age))



class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score
    def info(self):
        super().info()
        print('分数',self.score)
    def __str__(self):
        super().__str__()
        return '我的名字是{0},几年{1}岁'.format(self.name,self.age)

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):
        super().info()
        print('教龄',self.teachofyear)




stu=Student('张三',20,78)
print(stu)
tea=Teacher('李四',20,17)
stu.info()
tea.info()


class Animal(object):
    def eat(self):
        print("动物会吃")
class Dog(Animal):
    def eat(self):
        print('狗吃肉')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼..')

class Human:
    def eat(self):
        print('人吃五谷杂粮')


def fun(obj):
    obj.eat()

fun(Cat())
fun(Dog())
fun(Animal())
print('--------------------------------')
fun(Human())
































































