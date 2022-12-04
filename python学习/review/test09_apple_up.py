# python learing
# author:TNT
"""
求阶乘

"""
def fac(num):
    result = 1
    for num in range(1,num+1):
        result *= num

    return result

m = int(input("输入m = "))
n = int(input("输入n = "))
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数

print(fac(m)//fac(n)//fac(m-n))