# python learing
# author:TNT
from  math import sqrt
num = 2

while num < 100:
    is_prime = True
    end = int(sqrt(num))
    for x in range(2,end+1):
        if num % x ==0:
            is_prime = False
            break
        if is_prime:
            print(num)
    num += 1


