# python learing
# author:TNT
#内置函数：不需要加任何类名,直接进行使用
#range()函数:
#返回值为一个迭代器对象（数组),所以range对象的内存空间都是一样的，只有用到时才计算序列中的内容
#1:range(stop)-->创建一个[0，stop)之间的整数序列，步长为1
r=range(10)
print(r)
print(list(r))#list函数可以查看range中的序列
#2:range(start,stop)-->创建一个[start,stop)之间的整数序列,步长为1
r =  range(1,10)
print(list(r))
#3:range(start,stop,step)-->创建一个[start,stop)之间的整数序列,步长为step
r=range(1,10,2)
print(list(r))
'''判断指定的值是否存在(in /not in)'''
print(10 in r)
print(9 in r)
print(10 not in r)

#while for - in
#初始化变量0
#条件判断

a=1
sum=0

while a<101:
    #条件循环体
    print(a)
    if a%2==0:
        sum += a
    #改变变量
    a+=1
print(sum)

# for - in
for  i in 'range(1,101)':
    print(i)
for item in range(10):
    print(item)
for  _ in range(7):
    print('人生苦短,我用python')
sum1 =0
for i in range(2,101,2):
    sum1+=i

print(sum1)

#" / "就表示 浮点数除法，返回浮点结果;" // "表示整数除法。
for i in range(100,1000):
    ge = i%10
    shi = i//10%10
    bai = i//100
    # print(ge,shi,bai)
    if ge ** 3 + shi ** 3 + bai ** 3 == i:
        print(i)
'''从键盘键入密码,最多录入三次,如果正确就结束循环'''
# for item in range(3):
#     pwd = input('请输入密码:')
#     if pwd =='8888':
#         print('密码正确')
#         break
#     else:
#         print('密码不正确')
a=0
# while a<3:
#     pwd = input('请输入密码')
#     if pwd == '8888':
#         print('密码正确')
#         break
#     else:
#         print('密码不正确')
#     a+=1

'''------------------------------continue------------------------------'''
for item in range(1,51):
    if item % 5 != 0:
        continue
    print(item)





'''--------------------------else-------------------------'''
#else 可以与while for 搭配使用
# for item in range(3):
#     pwd=input('请输入密码:')
#     if pwd == '8888':
#         print ('密码正确')
#         break
#     else:
#         print('密码不正确')
# else:
#     print('对不起三次输入均不正确')

a = 0
# while a<3:
#     pwd = input('请输入密码:')
#     if pwd == '8888':
#         print('密码正确')
#         break
#     else:
#         print('密码不正确')
#     a+=1
# else:
#     print('对不起三次输入均不正确')
#
'''------------嵌套循环------------------'''

for i in range(1,4):#行表，执行三次，一次一行
    for j in range (1,5):
        print('*',end='\t')#不换行输出
    print() #换一行


for i in range(1,10):
    for j in range(1,i+1):
        print('i*j=%d'%(i*j),end='\t')
    print()











