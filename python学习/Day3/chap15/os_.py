# python learing
# author:TNT
import os
"""
调用操作系统
"""
# os.system('notepad.exe')
# os.system('calc.exe')
#
# #直接调用可执行文件
#
#
# os.startfile("C:\Program Files (x86)\网易云音乐PC版\cloudmusic.exe")
"""
getcwd()返回当前工作路径
listdir():返回指定路径下的文件和目录信息
mkdir():创建目录
rmkdir（）删除目录
makedirs()创建多级目录
removedirs()删除多级目录
chdir()s设计多级目录 
path{
abspath(path)
exits(path)
join(path,name)
splitext()
basename(path)
dirname(path)
isdir(path)



}
"""
print(os.getcwd())
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

