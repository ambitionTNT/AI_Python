
'''输入一个正整数判断是否为一个素数'''
from math import sqrt
num = int(input('请输入一个正整数：'))

mid = int(sqrt(num))
is_prime = True
for x in range(2,mid+1):
    if num % x == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print("是素数")
else:
    print("不是素数")




