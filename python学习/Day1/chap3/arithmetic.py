# python learing
# author:TNT

#input()函数的介绍
'''作用：接收来自用户的输入
返回值类型：输入的类型为str
值得存储:使用=对输入的值进行存储'''
#present = input('*#*#*#*#*#*#*')
#present = input('你想要什么礼物呢？')
#print(present)



#
# a =int(input('请输入第一个数'))
#
# b = int(input('请输入第二个数'))
# print(a+b)










#运算符：标准运算符,+ - * / % // **
print(1//2)
print(1/2)
print(1+2)
print(1//-6)#向下取整
print(1-1)
print(1*1)
print(2%2)

print(9%-4) # -3 公式：余数 = 被除数 - 除数 * 商 9-(-4)*(-3) 9-12--> -3
print(2**4)


#赋值运算符:运算顺序从右至左
# a = 3+4
#链式赋值
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))
#id(a)=id(b)=id(c)在堆上只有一个对象，而使用了三个引用


#参数赋值
a=20
a+=30
print(a)
a-=20
print(a)
a*=20
print(a)
b=2.0
b%=3
print(b)




#支持系列解包赋值
#左右变量个数和值得个数应该要对应
a,b,c=2,3,4
print(a,b,c)

#例：交换两个变量的值
a,b=10,20
print(a,b)
a,b=b,a
print(a,b)





# 比较运算符 < > + >= <= ==
#==:两个变量的的值value
#is/is not:比较的为两个变量的标识id

a,b=20,10
print('a>b？',a>b)
print('a<b?',a<b)
a,b=10,10
print(a==b)# True

print(id(a),id(b))#id 相等
print(a is b) #True


list1=[11,22,33,44]
list2=[11,22,33,44]
print(list1==list2)
print(list1 is list2)
print(list1 is not list2)
print(id(list1),id(list2))






#bool运算符:and/or/not/not in /in
#位运算符:&、|、^、~、>>、<<
a,b=1,2
print('-------')
print(a==1 and b==2)
print(a==1 or b== 2)



print(4&8)
print(4|8)
print(4>>7)


#优先级:算术优先级（**，*，/,\\,% +,-)>位运算（<<,>>,&,|)>比较运算符（<，>,<=,>=,==,!=)>bool运算符(and or not )>赋值运算符(=)


















