# python learing
# author:TNT
import math
"""
以.py结尾的文件，尽量不要与python自带的标准模块名称相同

导入模块：
import 模块名称 [as 别名]

from 模块名称 import 函数/变量/类

以主程序形式运行：
在每个模块的定义中都包含一个记录模块名称的变量__name__，程序可以检查改变量,以确定他们在那个模块中执行。如果一个模块不是被导入到其他 程序中
执行，那么它可能在解释器的顶级模块中执 bhrsx行。顶级模型的__name__变量的值为__main__
if __name__= '__main__:
    pass



python中的包
包是一个分层次的目录结构，它将一组功能相近的模块组织在一起
代码规范
避免模块名称冲突
包与目录的区别：
包含__init__.py文件的目录称为包
目录里通常不包含__init__.py文件
包的导入
import 包名.模块名
python{包{模块{函数 属性}}}


---------------------------
使用import 方式进行导入时，只能跟包名或者模块名
使用from  import 可以导入包模块，函数，变量
"""
def fun():
    pass

def fun1():
    pass

class Student:
    native_place = '安徽'
    def eat(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def cm(cls):
        pass
    @staticmethod
    def sm():
        pass
print(math.pi)
print(dir(math))
print(math.pow(2,3))
print(math.ceil(9.1))
print(math.floor(9.9))





































































































