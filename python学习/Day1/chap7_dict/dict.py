# python learing
# author:TNT
"""字典
字典是python内置的数据结构之一,与列表一样是一个可变序列
以键值对的方式存储数据，字典是是一个无序的序列
实验{}来定义
根据键去查值
"""

#创建字典
scores = {'张传龙':100,'Jack':99,'潘苗':99}
print(scores)
print(type(scores))
dict(name='jack',age =10)
'''---------------获取————————————————————————————————'''
#[],不存在会异常
#get()，不存在返回None
print(scores['张传龙'])
print(scores.get('张传龙'))

#键的判断
print('张传龙' in scores)
print('张传龙' not in scores)
del scores['张传龙']#一删是一对
print(scores)
scores['Tom']=100
print(scores)
scores['Rose']=90
print("---")
print(scores['Tom'])
#获取所有的key
keys=scores.keys()
print(type(keys))
print(list(keys))#将所有的key组成的视图转换为列表
#获取所有的value
# values =scores.values()
# print(values)
# print(type(values))
# print(list(values))
#获取所有的键值对
items=scores.items()
print(items)
print(list(items))#转换之后的元素有元组组成
"""-----------------遍历----------------------------"""

for item in scores:
    print(item,scores[item],scores.get(item))

for key in scores.values():
    print(key)
""""特点:
    键不允许重复
    值可以重复
    字典中的元素是无序的
    字典中的key必须是不可变对象
    字典也可以根据需要动态伸缩
    字典会浪费较大的内存，是一种使用空间换时间的数据结构
    


"""
"""----------字典生成式---------"""
"""zip()内置函数，用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组。然后返回有这些元组组成的列表"""

#
#
items=['Furits','Books','Others']
prices=[98,78,67]
lst=zip(items,prices)
print(list(lst))
d={item.upper(): price for item,price in zip(items,prices)}
print(d)













































