# python learing
# author:TNT
'''我们还可以实现将一个正整数反转，例如：将12345变成54321，代码如下所示。'''


num = int(input("请输入一个正整数:"))

reserver_num = 0
while num>0:
    reserver_num = num % 10 + reserver_num*10
    num = num // 10



print(reserver_num)

