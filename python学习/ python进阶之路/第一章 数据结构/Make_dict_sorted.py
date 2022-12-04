# python learing
# author:TNT
from collections import OrderedDict
from random import randint
from time import time

d = OrderedDict()



players = list('ABCDEFGH')
start = time()

for i in range(8):
    input('用户答题:')
    p = players.pop(randint(0, 7-i))
    end=time()
    print(i +1, p, end-start)

    d[p] = (i+1, end-start)


print(d)
for item in d.items():
    print(item)
for v, k in d.items():
    print(v )
    print(k)





