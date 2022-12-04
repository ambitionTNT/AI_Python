# python learing
# author:TNT
"""字符串是个不可变的字符序列"""
#内存中相同的字符串只有一份
'''这就是字符串驻留机制
符合标识符的字符串
0、1长度


'''
a='站内不关窗口'
b='张传龙'
c="张云蕾"
e="""张云蕾"""
d='''周大锤'''
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d))
print(e,id(e))

print(a.index('内'))#子串第一次出现的位置，不存在抛出异常
print(a.find('内'))#子串第一次出现的位置，不存在 返回-1
print(a.rfind('内'))#子串最后一次最后一次出现的位置，不存在，返回-1
print(a.rindex('内'))#子串最后一次出现的位置，不存在抛出异常


"""转换后会产生一个新的字符串对像"""
#upper() 大写
#lower() 小写
#swapcase()大变小，小变大
#capitalize()把第一个字符转换为大写，把其余的字符转换为小写
#title()把每个单词的第一个字符转换为大写，把其余的字符转换为小写

'''
center()居中对齐,第一个参数为宽度，第二个是填充符
ljust()左对齐，
rjust()右对齐
zfill()右对齐,0填充


'''
"""字符串的分割
返回列表
splist()左侧开始
rsplist()右侧开始


"""

s1='hello|world|Python'
s2='hello world Python'
# print(s2.split())
# print(s1.split(sep='|',maxsplit=2))
# print(s2.rsplit())
# print(s1.rsplit(sep='|',maxsplit=1))
#
# """判断是否为合法的标识符
#
#
# """
# print('1',s1.isidentifier())
# print('2',s2.isidentifier())
# print('3','Jack'.isidentifier())
# print('4','\t'.isspace())
# print('5','张传龙'.isalpha())
# print('6','123'.isdecimal())
# print('7','123123123kdhsf'.isalnum())
print(s1.replace('Python','java'))
#print('',join(s2)) 列表、元组的字符串合并
lst=['hello','world']
print(' '.join(lst))


"""字符串的比较"""
#ord()原始值,chr()
print('apple'<'appla')
str ='hello world'
#切片
str1=str[:4]
str=str[1:6:2]
#str1=str1+'!'+str
print(str1)
print(str)

"""格式化字符串"""
'''
%作为占位符
%d，i 整数
%f   浮点数
%s   字符串

'''

name='jack'
age=20
print('我叫%s,今年%9d岁' %(name,age))#可以表示宽度与小数的精度


#{}
print('我叫{0},今年{1}岁'.format(name,age))
print(f'我叫{name},今年{age}岁')

print('{:.3}'.format(3.1415926))

"""字符串的编码转换"""

"""
编码：将字符串转换为二进制数据(bytes
解码：将bytes类型的数据转换成字符串类型
"""
s='我是人间惆怅客'
#编码:
# print(s.encode(encoding='GBK'))#在gdk这种编码格中，一个中午站两个字节
# print(s.encode(encoding='UTF-8'))#在UTF-8这中编码中，一个中文占三个字节

#解码
#byte代表就是一个二进制数据（字节类型的数据）
byte=s.encode(encoding='GBK')#编码
print(byte)
print(byte.decode(encoding='GBK'))#解码











