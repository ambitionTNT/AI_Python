# python learing
# author:TNT
import schedule
import sys
import  time
import os
import urllib

"""

常用的模块：
sys:与python解释器及其环境操作相关的标准库
time:提供与时间相关的各种函数的标准库
os:提供了访问操作系统服务功能的标准库
calendar:提供与日期相关的各种函数的标准库
urllib:用于读取来自网上（服务器）的数据标准库
json：用于使用json序列化和反序列化对象
re：用于在字符串指向正则表达式匹配和替换
math：提供标准算术运算函数的标准库
decimal：用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算
logging：提供了灵魂的记录事件、错误、警告、和调试信息等信息的功能


第三方模块的安装和使用
pip install 模块名

使用：
import 模块名










"""
import pack1.module_A
print(pack1.module_A.a)

print(sys.getsizeof(24))
print(time.localtime())

def job():
    print('呵呵______________')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)