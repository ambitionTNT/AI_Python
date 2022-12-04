# python learing
# author:TNT
#类：分门别类，类就是由多个实物组成群体的统称
#能够帮助我们快速理解和判断事物的特征
#数据类型：不同的数据类型属于不同的类
#对象：某类的个例，实例
#python是一切皆对象

"""
类属性：类中方法外的变量称为类属性被该类的所以对象所共享
类方法：使用@classmethod修饰的方法,使用类名直接访问的方法
静态方法：使用@staticmethod修饰的方法，使用类名直接访问的方法






"""
class Student:#类名，多个单词组成，首字母大写
    native_pace='安徽'#直接卸载类的变量，称为类属性
    #在类之外定义的称为函数,在类内定义的称为方法

    def __init__(self,name,age):
        #self.name称为实体属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.name=name
        self.age=age


    def eat(self):
        print('学习。。。')


    #静态方法
    @staticmethod
    def method():
        print('静态方法')
    @classmethod
    def drink(cls):
        print('方法')




print(Student,id(Student),type(Student))
print("--------------------------")

"""对象的创建"""
stu1=Student('张艹',20)
print(stu1)
print(id(stu1))
print(type(stu1))

print("----------------------------")
print(stu1.name)
print(stu1.age)
print(stu1.eat())
print(stu1.method())
print(stu1.drink())
Student.eat(stu1)

#类属性的使用方法

stu2=Student('李丹',20)
print(stu1.native_pace)
print(stu2.native_pace)
print('----------------------类方法----------------------')
Student.cm()


print('----------------今天发发')




































