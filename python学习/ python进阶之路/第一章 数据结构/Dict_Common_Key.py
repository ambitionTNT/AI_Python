# python learing
# author:TNT
from functools import reduce
from random import  randint,sample



print(sample('abcdefg', randint(3,6)))
print('-----')
dict1 = {x : randint(1,4)for x in sample('abcdefg', randint(3, 6))}
print(dict1)

dict2 = {x : randint(1,4)for x in sample('abcdefg', randint(3, 6))}
print(dict1)

dict3 = {x : randint(1,4)for x in sample('abcdefg', randint(3, 6))}
print(dict3)


res = []
for k in dict1:
    if k in dict2 and k in dict3:
        res.append(k)



print(res)
print('---------------------------------------------------------')

print(dict1.keys() & dict2.keys() & dict3.keys())


print("--------------------------------")


print(list(map(dict.keys, [dict1, dict2, dict3])) )

print(reduce(lambda a,b: a & b, map(dict.keys, [dict1, dict2, dict3])))















