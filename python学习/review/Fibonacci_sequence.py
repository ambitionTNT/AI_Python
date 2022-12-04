# python learing
# author:TNT
'''生成斐波那契数列的前20个数。'''
num = 0;
first = 1
second = 1
print(first)
print(second)
while num<20:

    third = first + second
    print(third)
    first = second
    second = third
    num += 1

