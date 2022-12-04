# python learing
# author:TNT
'''完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。'''

factor = 0
flag = 1
for x in range(1,1001):
    flag = 1
    for i in range(2,x//2+1):
        if x % i == 0:
            flag += i;
    if ( flag == x ):
        print(x)
