# python learing
# author:TNT
from collections import Counter
from random import randint

data = [randint(0,20) for _ in range(30)]
data1 = [0 for _ in range(30)]
print(data)
print(data1)
print(len(data))

c = dict(zip(data, data1))

c2= Counter(data)


print("------------使用counter进行统计")
print(c2)


print("统计出前三名=-------------------")
c3 = c2.most_common(3)
print(c3)