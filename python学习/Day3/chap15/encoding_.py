# python learing
# author:TNT
"""
python操作文件：
1.打开或者新建文件
2.读写文件
file =open(filename [,mode,encoding]
r:只读
w:只写，不存在在建立
a：追加
b：二进制
read() 读文件，省去参数读到末尾
readline() 从文本文件读一行
readlines():每行为列表的内容
write():写
writelines（）：将字符串列表s_list写入文本文件，不添加换行符
seek()：把文件指针移到新的位置上
tell():返回文件指针当前的位置
flush:把缓冲区的内容写入文件，但不关闭文件
 """
file=open('D:\\test.txt','r+')
file.write('hi,sb')
for i in file.readlines():
    print(i)

file.close()









