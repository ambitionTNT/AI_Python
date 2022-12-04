# python learing
# author:TNT
"""

浅拷贝：只拷贝源对象
深拷贝: 全拷贝
"""
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

#1.变量的赋值
cpu1=CPU()
cpu2=cpu1#新的引用，不是对象
print(cpu1)
print(cpu2)
disk=Disk()
computer = Computer(cpu1,disk)
#2.浅拷贝
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
#3.深拷贝
computer3=copy.deepcopy(computer)











































































