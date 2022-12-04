# python learing
# author:TNT

# 浅拷贝
import copy

list1 = [1, 2, 3]
list2 = list(list1)
print(list2)
print("list1 == list2 ?", list1 == list2)
print("list1 is list2 ?", list1 is list2)


set1 = set([1, 2, 3])
set2 = set(set1)
print(set2)
print("set1 == set2 ?", set1 == set2)
print("set1 is set2 ?", set1 is set2)

dict1 = {1: [1, 'w'], 2: 0, 3: 90}
dict2 = dict(dict1)
print(dict2)
print("dict1 == dict2 ?", dict1 == dict2)
print("dict1 is dict2 ?", dict1 is dict2)



print("-----------------------------------------")
# 对于列表，还可以通过切片操作符“：”来完成浅拷贝
list1 = [1, 2, 3]
list2 = list1[:]
print(list2)
print("list1 == list2 ?", list1 == list2)
print("list1 is list1 ?", list1 is list2)
# 使用 copy.copy() 函数

set1 = set([1, 2, 3])
set2 = copy.copy(set1)
print(set2)
print("set1 == set2 ?", set1 == set2)
print("set1 is set2 ?", set1 is set2)

print("-------------------------------------------------------------------")
# 对于元组，使用 tuple() 或者切片操作符 ‘:’ 不会创建一份浅拷贝，相反它会返回一个指向相同元组的引用：
tuple1 = (1, 2, 3)
tuple2 = tuple(tuple1)
print(tuple2)
print("tuple1 == tuple2 ?", tuple1 == tuple2)
print("tuple1 is tuple2", tuple1 is tuple2)
'''
使用 tuple() 或者切片操作符 ‘:’ 不会创建一份浅拷贝，因为它开辟新的内存存储的是原对象的引用，
而没有创建新的对象来存储原对象的子对象的引用，所以不是浅拷贝。相反它会返回一个指向相同元组的引用。
'''
print("-------------------------------------------------------------------")
str1 = 'operation'
str2 = str1[:]
print(str2)
print("str1 == str2 ?", str1 == str2)
print("str1 is str2 ?", str1 is str2)

str1 = 'operation'
str2 = str(str1)
print(str2)
print("str1 == str2 ?", str1 == str2)
print("str1 is str2 ?", str1 is str2)

str1 = 'operation'
str2 = copy.copy(str1)
print(str2)
print("str1 == str2 ?", str1 == str2)
print("str1 is str2 ?", str1 is str2)
'''
也就是说，对字符串和元组使用 copy（）、[:]、本身的构造器完成的复制，都只是开辟了内存存储原对象的引用，而不是存储原对象的子对象的引用。
'''

# 切片操作符 ‘:’ 不能用于字典和集合完成浅拷贝
#
# set1 = {1, 2, 3}
# set2 = set1[:]
# print(set2)

print('-------------------------------------------------------------------------------------------------------------------')
set1 = {1: 1, 2: 2, 3: 3}
set2 = set1
print(set2)
print("set1 == set2 ?", set1 == set2)
print(id(set1))
print(id(set2))

# Python 中以 copy.deepcopy() 来实现对象的深度拷贝

list1 = [[1, 2], (30, 40)]
list2 = copy.deepcopy(list1)


list1.append(1009)
print("list1: ", list1)
print("list2: ", list2)

list1[0].append(34)
print("list1: ", list1)
print("list2: ", list2)
list1[1] += (50, 60)
print("list1:", list1)
print("list2:", list2)