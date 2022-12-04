# python learing
# author:TNT
#列表是一个大容器，可以存储N多个元素,程序可以方便的对这些数据进行整体操作
#列表相当于其他语言中的数组
#索引（正负索引）,数据
#列表中存储的是n个对象的引用


#lst 也是个引用,它引用一个列表，列表中放了三个对空间对象的引用，分别引用是三个对象
#列表的创建：
#使用中括号,调用内置函数list(),使用，进行分隔
'''--------------特点----------------'''
"""
    列表元素按顺序有序排序
    索引映射唯一的数据
    列表可以存储重复数据
    任意数据类型混存
    根据需要动态分配和回收内存
"""



lst1 = list(['hello','world',98,89,98,20,10])
lst2=['hello','world',98]

#index可以获取列表相应元素的索引
#当不存在时抛出异常
#在start 和 stop之间进行查找[start,stop)




print(id(lst1))
print(type(lst1))
print(lst1)
for item in lst2:
    print(item)



#index可以获取列表相应元素的索引
#当不存在时抛出异常
#在start 和 stop之间进行查找[start,stop)
print(lst1.index('hello'))
print(lst2.index('hello',0,3))
#print(lst1.index('hell'))

'''----------------列表切片--------------'''
'''列表名[start:stop:step]'''
"""----------特点-----------------"""
"""
    切片的结果：原来列表的拷贝
    切片的范围：[start,stop)
    step默认为1
    
    

"""

#lst1 = list(['hello','world',98,89,98,20,10])
print("--------------------")
lst3=lst1[1:4]
print(id(lst1))
print(id(lst3))
print(lst1[1:4:])
print(lst1[0:4:2])
#步长为正默认为列表的第一个元素
print(lst1[:4:2])
print("----------")
print(lst1[1::2])
#步长为负默认为最后一个元素
print("origin:",lst1)
print(lst1[::-1])
'''--------------------元素查询--------------------hn'''
print(10 in lst1)
for item in lst1:
    print(item)
'''----------添增修改删除---------------------------------'''
print(lst1)
#append():在末尾添加一个元素
#extend():在末尾至少添加一个元素
#insert():在列表的任何一个位置添加
#切片:插入至少一个元素
lst1.append(100);
for i in '潘苗是我女朋友':
    lst1.append(i)
print(lst1)
#lst3作为一个元素加入
print(lst3)
lst1.append(lst3)
lst1.extend(lst3)
lst1.insert(1,'张传龙')
print(lst1)
#把1:以后的给切掉了，然后在添加上去
lst1[2:]=lst3
print(lst3)
print("----------")
print(lst1)

#remove()一次删除一个元素，重复元素只删除一个，元素不存在抛出异常
#pop()删除一个指定索引位置上的元素，不指定索引救世主最后一个元素
#切片：一次至少删除一个元素
#clear()清空列表:
#del 删除列表
lst1.remove('hello')
print("----------")
print(lst1)
for i in '潘苗是我女朋友':
    lst1.append(i)
lst1.pop(1)
print(lst1)
lst1.pop()
print(lst1)

lst1=lst1[2:8]
#lst1.clear()
# del lst1
print(lst1)
lst1.append('友')
print(lst1)
lst1[0]='潘'
print(lst1)

# '''------------------排序-------------------------------'''
# #调用sort()函数
# #sorted()对列表进行排序,将产生一个新的列表对象
# lst1.sort(reverse=True)#表示降序,false是正序
# print(lst1)
# print(id(lst1),type(lst1))
# lst1=sorted(lst1)
# print(id(lst1),type(lst1))
#
# '''----------------列表生成式----------------------------------'''
# lst4=[ i for i in range(10)]
# print(lst4)
#
# lst5=[ i*i for i in range(10)]
# print(lst5)
#










