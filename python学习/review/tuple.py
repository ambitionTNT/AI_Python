# python learing
# author:TNT
# 定义元组
t = ('骆昊', 38, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
# t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('王大锤', 20, True, '云南昆明')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 25
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
print("------------------------------")
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)
print("-----------------------------------------")
set1.add(4)
set1.add(5)
print("---------------------------")
print(set2)
set2.update([11, 12])
print(set1)
print(set2)
set2.discard(5)
print("-----")
print(set2)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)

print("-----------------------------------------------")
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
print(set1.intersection(set2))
print(set1.union(set2))
print(set2 | set1)
print(set1)
print(set2)
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1^set2)
# 判断子集和超集
print(set2 <= set1)
print(set2.issubset(set1))
print(set3 <= set1)
print(set3)
print(set3.issubset(set1))
print("-------------------------------------------------------------------")
scores = {'张传龙':95,'白元芳':78,'狄仁杰':82}
print(scores)
# 创建字典的构造器语法
items = dict(one=1,two=2,three=3,four=4)
print(items)
items2=dict(zip(['a','b','c'],'123'))
print(items2)
#创建字典的推导式语法
items3={num:num**2 for num in range(1,10)}
print(items,items2,items3)
# 通过键可以获取字典中对应的值
print(scores['张传龙'])
print(scores['狄仁杰'])
for key in scores:
    print(f'{key}:{scores[key]}')
scores.update(冷面=67,傻逼=23)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])

print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
# 清空字典
scores.clear()