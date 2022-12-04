# python learing
# author:TNT
#最大公约数
def gcd(x,y):
    if( x > y):
        (x,y) = (y,x)
    for factor in range(x,0,-1):
        if x % factor ==0 and y % factor ==0:
            return factor

#求解最小公倍数
def lcm(x,y):
    return x*y // gcd(x,y)


print(gcd(6,12))
print(lcm(6,12))



