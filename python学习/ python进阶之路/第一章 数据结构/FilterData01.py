# python learing
# author:TNT

from random import randint
from timeit import timeit

from urllib3.connectionpool import xrange

data = [8, 32, 4, -45, -3, 23, 345, 3, 12, 56]
res = []

for x in data:
    if x >= 0:
        res.append(x)



data = [randint(-10, 10) for _ in xrange(10)]

print(data)








