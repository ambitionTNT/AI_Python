# python learing
# author:TNT
from collections import Iterable

import requests
import json
'''
可迭代对象：生成器，元组，列表，集合
迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。



生成器就是为了节省内存，是迭代器的一种，生成器也是迭代器





'''
'''
判断是否是可迭代的：
isinstance()
'''


list1 = [1, 2, 3, 4]
s = 'qweqweqw'
f = isinstance(list1, Iterable)
print(f)
print(isinstance(s, Iterable))



# 生成器


g = (x+1 for x in range(10))
print(next(g))
print(isinstance(g, Iterable))

print(type(iter(list1)))
print(type(iter(s)))
t = iter(list1)
#迭代器中有两个函数 next() __next__
print(t.__next__())
print(next(t))


# def getWeather(city):
#     rb=requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
#
#     data = json.loads(rb.text)
#     # 访问今天的天气情况
#     print(data['data']['forecast'][0][type])
#
#
#
#
# getWeather('北京')
