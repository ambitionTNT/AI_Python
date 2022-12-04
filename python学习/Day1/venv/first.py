print("hello world")
#可以是数字,表达式,字符串
#引号的意思是告诉计算机这玩意不需要你理解，输出就行了

print("520")


#输出表达式
print(7*3)



#输出到文件中
#输出流
fp=open('D:/test.txt','a+')
#注意点：要有盘符，指定file=fp
print('我恨你 周涛',file=fp)
fp.close()

#不进行换行输出,使用,分隔，不换行
print("hello ",'world','python')

#转义字符：\m,\r,\t,\b
print('hello\nworld')#换行
print('hello\tworld')#制表符,四个位置为一个制表位
print('hellooooo\tworld')
print('hello\rworld')#回车:world把hello 覆盖掉了
print('hello\bworld') #\b是退了一个格

print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')

#原字符，不希望转义字符起作用,在字符串之前加上r/R
print(r'hello\nworld')












