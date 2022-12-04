# python learing
# author:TNT
from collections import namedtuple
'''


生成可以使用名字来访问元素内容的tuple子类，
命名元组赋予每个位置一个含义，提供可读性和自文档性。
它们可以用于任何普通元组，并添加了通过名字获取值的能力，通过索引值也是可以的。
'''
'''使用类对象的方式存储元组'''
Student = namedtuple('Student', ['NAME', 'AGE', 'SEX', 'EMAIL'])
s = Student('jam', 16, 'male', 'jim8998@gmail.com')
s2 = Student('jack', 26, 'male', 'jackw41234@gmail.com')
print(s)
print(s2)
print(s.NAME)
print(s2.NAME)