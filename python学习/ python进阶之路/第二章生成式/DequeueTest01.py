# python learing
# author:TNT
from collections import deque

d = deque('ghi')
d.append('j')
print(d)
d.appendleft('F')
print(d)
d = deque('xiaoweuge')

e = d.copy()
d.append('A')
e.append('B')
print(d)
print(e)

d = deque('Hello World')
print(d.count('l'))
#扩展deque的右侧，通过添加iterable参数中的元素。\\\
a = deque('abc ')
b = deque('ef')
a.extend(b)

print(a)

#与append 的区别

a.append(b)
print(a)


# 扩展deque的左侧，通过添加iterable参数中的元素。注意，左添加时，在结果中iterable参数中的顺序将被反过来添加。
print('-----')
a = deque('abc ')
b = deque('ef')
a.extendleft(b)
print(a)
'''
index()
返回 x 在 deque 中的位置（在索引 start 之后，索引 stop 之前）。 返回第一个匹配项，如果未找到则引发 ValueError。
'''

d = deque('xiaoweuge')
print(d.index('w'))
# 9、insert()
# 在位置 i 插入 x 。
#
# 如果插入会导致一个限长 deque 超出长度 maxlen 的话，就引发一个 IndexError。

a = deque('abc')
a.insert(1,'X')
print(a)
'''
popleft()
移去并且返回一个元素，deque 最左侧的那一个。 如果没有元素的话，就引发 IndexError。
'''

print(a.popleft())
print(a)
print(a.pop())
print(a)

'''
remove(value)
移除找到的第一个 value。 如果没有的话就引发 ValueError。

'''
print("--------------------")
a = deque('abca')
print(a.remove('a'))
print(a)
'''


reverse()
将deque逆序排列。返回 None 。
'''
d = deque('ghi') # 创建一个deque
l = list(reversed(d))
print(l)
print(deque(reversed(d)))