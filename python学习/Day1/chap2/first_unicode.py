# python learing
# author:TNT
import keyword

print(keyword.kwlist)
print(chr(0b100111001011000))
print(ord('乘'))
#保留字:有些单词不能用，是被python使用了
#自己可以使用的叫做标识符
#变量:一个容器

#内存分析图:
name="king"
print(name)
print(id(name))
print('标识',type(name))
print('值',name)
#当多次赋值会，变量会被指向不同的地址空间
#数据类型:int float bool str

#整数类型:integer
#可以表示 整数 负数 零
n1 = 90
n2 = -89
n3 = 0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
#整数可以表示为二进制,十进制,八进制,十六进制
print('十进制',119)
print('二进制',0b10101010)
print('八进制',0o123112345)
print('十六进制',0x31234124abcd)



#浮点类型:float
a = 3.14159
print(a,type(a))
print(id(a))


from decimal import  Decimal
n1=1.1
n2=2.2
print(n1+n2)


print(Decimal(n1)+Decimal(n2))

print(Decimal('1.1')+Decimal('2.2'))



#布尔:boolean
# True or  False
f1 = True
f2 = False

print(f1,type(f1))
print(f2,type(f2))
print(f1+f2)


#字符串类型:string
#不可变的字符序列
#可以使用单引号,双引号,三引号'''/"""来定义
#单引号和双引号定义的字符串必须在一行
#三引号定义的字符串可以分布字连续的多行
str1="人生苦短,我用python"
str2='人生苦短,我用python'
str3='''人生苦短,
我用python'''
str4="""人生苦短,
我用python"""
print(str1)
print(str2)
print(str3)
print(str4)

#数据类型的转换
#str()-->转换为字符串类型
#int()-->转换为int类型,不能转换为string的数字串类型，只能转换数字串
#float()-->转换为浮点类型,要求同上
name='张三'
age=20
print(type(name),type(age))
print('我是'+name+
      '今年'+str(age)+'岁')

s1='12'
print(float(s1),type(s1))
print(str(f1),type(f1))
#注释：中文编码声明在开头的注释:#coding = utf-8
