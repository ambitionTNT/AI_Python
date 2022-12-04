# python learing
# author:TNT
from random import randint

data = [randint(0, 20) for _ in range(30)]
data1 = [0 for _ in range(30)]
print(data)
print(data1)
print(len(data))
print("----")
c = dict(zip(data, data1))
print(c)
print(len(c))
for x in data:
    c[x] += 1


d = [(k, v) for k, v in c.items()]
print(d)
d_sorted = sorted(d, key=lambda x: x[1], reverse=True)
print(d_sorted)



e = list(zip(c.keys(), c.values()))
print("---")
print(e)

print("-----首先将字典转换为列表--------")

e_sorted = sorted(e, key=lambda x :x[1],reverse=True)
print(e_sorted)

print("----直接对字典进行排序----")
print(c)
f = sorted(c.items(), key=lambda  x:x[1], reverse=True)
print(f)