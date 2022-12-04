# python learing
# author:TNT
#python 一切皆是对象，所以对象都有一个bool 值，获取对象的布尔值，用内置函数bool()
#以下对象的bool值为False
'''
False
数值0
None
空字符串
空列表
空元组
空字典
空集合
'''


print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))#空列表
print(bool(list()))#空列表
print(bool(tuple()))#空元组
print(bool(dict()))#空字典
print(bool(set()))#空集合