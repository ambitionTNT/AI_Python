# python learing
# author:TNT
'''-----------集合---------------'''
'''python语言提供的内置数据结构
与列表、字典一样都属于可变类型的序列
集合是没有value的字典
集合元素不允许重复'''
'''创建
b={}
s=set()
'''
s5=set({12,23,45})
s={'I','love','you'}
s1=set(range(6))
print(s1,type(s1))
s2=set([1,2,3,4,5,6])#列表转换成集合
print(s2,type(s2))
s3=set((1,2,3,4,5,6,6))#元组转换成集合
print(s3,type(s3))
s4=set('python')
print(s4)


#空集合
s6=set()
print(s6)


"""'-------------------集合的相关操作--------------"""
print('I' in s)
print('I' not in s)
#not in /in 判断集合元素的操作
#调用add(),添加一个
#调用update()，至少添加一个
s.add('hhh')
s.update('zzz')
#添加列表
s.update([10,10,30])
#添加元组
s.update((28,293,440))
print(s)
#remove()删除指定的元素，不存在将抛出异常
#discard()删除指定元素，不纯在没有异常
#pop()删除任意的一个元素
#clear()清空元素
s.remove(10)
print(s)
s.discard(90)
print(s)
s.pop()
print(s)
"""-----------集合的关系-----------------"""
#使用==，!=来判断
#子集判断:issubset()
#判断超集 issuperset()
#判断交集：isdisjoint()
s1={10,30,40,560,69}
s2={10,40}
print(s2.issubset(s1))
print(s1.issuperset(s2))
s1={10,30,40,560,69}
s2={10,40}
'''--------------数学操作---------------'''
#交集
print(s1.intersection(s2))
print(s1&s2)
#并集
print(s1.union(s2))
print(s1|s2)
print(s1)
print(s2)
#差集
print(s1.difference(s2))

#对称差集
print(s1.symmetric_difference(s2))
'''---------集合生成式----------------'''

#列表生成式
lst=[i*i for i in range(9)]
print(lst)
#集合生成式
s={i*i for  i in range(9)}
print(s)

























































