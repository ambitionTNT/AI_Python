# python learing
# author:TNT
from random import randint

my_dict = {x: randint(60, 100) for x in range(1, 21)}
print(my_dict)
my_dict1 = {k: v for k, v in my_dict.items() if v > 90}
print(my_dict1)

data = [8, 32, 4, -45, -3, 23, 345, 3, 12, 56]
s = set(data)
s1 = {x for x in s if x % 3 == 0}
print(s1)
