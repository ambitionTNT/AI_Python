# python learing
# author:TNT
"""
python 是动态语言，在创建对象之后，可以动态的绑定属性和方法
"""
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在拉屎')



stu1=Student('张三',30)
stu2=Student('李四',20)

print('------------------stu2动态绑定性别属性------------')
stu2.gender='女'
print(stu2.name,stu2.gender,stu2.age)
print('------------------动态绑定方法-------------------')
def show():
    print('定义在类之外的，称为函数')
stu1.show=show
stu1.show()

































































