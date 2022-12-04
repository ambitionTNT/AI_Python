# python learing
# author:TNT

"""function"""
"""
执行特定任务已完成特定功能的一段代码
代码复用
隐藏实现细节
提高可维护性
提高可读性便于调试
def 函数名 （[输入参数 ]）:
    函数体
    [return xxx]
    
函数参数传递：
    
"""
def calc(a,b):
    c=a+b
    return c
result=calc(3,4)#顺序传递
res=calc(b=3,a=4)#关键字传递
print(res)
print(result)


def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1',arg1)
    print('arg2',arg2)

n1=11
n2=[22,33,44]
fun(n1,n2)#位置传参

print('n1',n1)
print('n2',n2)
"""
如果是不可变对象，在函数体的修改不会影响实参的值，arg1的修改为100不会影响n1的值
如果是可变对象，在函数体的修改会影响实参的值，arg2的修改，append(10),会影响到n2的值
元组的引用不变
函数返回多个值时，结果为元组
"""
def fun1(num):
    odd=[]
    even=[]
    for i in range(num):
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even


print(fun1(8))
"""
函数的返回值
1.如果函数没有返回值[函数执行完毕后，不需要给调用处提供数据] return 可以省略不写
2.函数的返回值，如果是一个，直接返回类型
2.函数的返回值，如果是一个，返回的结果是元组

"""
"""
函数的参数定义
函数定义默认值参数
函数定义是，给形参设置默认值，只有与默认值不符的时候才需要传递实参


个数可变的位置参数
    函数定义是，可能无法事先确定传参的个数，可以使用可变的位置参数
    使用*定义个数可变的位置形参
    结果为一个元组
def fun3(*arg):
    print(arg)
    
个数可变的关键字形参
    定义函数时，无法事先确定传递的关键字实参的个数时，可以使用可变
    的关键字形参
    使用**定义个数可变的关键字形参
    结果为一个字典
    
    在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求，个数可变的位置形参，放在
    个数可变的关键字形参之前
    
def fun4(**arg):
    print(arg)
"""
def fun2(a,b=10):
    print(a,b)
fun2(100)
fun2(20,20)
print()

def fun3(*arg):
    print(arg)
fun3(10,10,1001,101,0)

def fun4(**arg):
    print(arg)

fun4(a=10)
fun4(b=10,c=10,d=10)

def fun(a,b,c):
    print(a)
    print(b)
    print(c)
fun(10,10,10)
lst=[10,22,33]
fun(*lst)#在函数调用时，将列表中的每个元素都转换为位置实参传入
print('----------------------')
dic={'a':111,'b':222,'c':333}
fun(**dic)#在函数调用是，将字典中的键值对都转换为关键字实参传入

def fun6(a,b=19):
    print(a)
    print(b)
def fun7(*args):
    print(args)
fun7(10,10,10,10,10,10,10,10,10,10,10)

def fun8(**args):
    print(args)
fun8(a=11,b=11,c=2,d=2)

def fun9(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
#调用fun9函数
fun9(10,20,c=20,d=90)
"""需求，c,d只能关键字传递"""
def fun10(a,b,*,c,d):
    pass#在*之后的参数，在函数调用是，只能采用关键字参数

def fun11(*args,**args2):
    pass
def fun12(a,b=10,*args,**args2):
    pass


"""
变量的作用域：

"""
"""递归"""
def fac(n):
    if n==1:
        return  1
    else:
        n*fac(n-1)
def fib(n):
    if n<=2:
        return  1
    else:
        return fib(n-1)+fib(n-2)

print(fib(8))

for i in range(1,7):
    print(fib(i))


















