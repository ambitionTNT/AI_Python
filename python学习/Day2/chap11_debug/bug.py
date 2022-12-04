# python learing
# author:TNT
"""
1.SyntaxError:粗心导致的
2.知识掌握不精练,细而杂乱：practice  practice and practice
3.思路不清晰，
    使用#注释掉部分代码
    print()查看程序是否正常执行，对错误程序进行查找
4.异常牛逼！！！！！！！！！！！
try:可能会出现异常的程序
except:发生异常执行的程序

"""
"""
try:
    a=int(input('请输入一个整数'))
    b=int(input('请输入一个整数'))
    result=a/b
    print(result)
except ZeroDivisionError:
    print('输入有误')
except ValueError:
    print('')
except:
    BaseException
print('程序结束')
"""

"""
try:
except:
else:


try:
    a=int(input('请输入一个整数'))
    b=int(input('请输入一个整数'))
    result=a/b
except BaseException as e:
    print('出错了')
else:
    print('计算结果为：',result)

    """



"""
try:
except:
else:
finally:


try:
    a=int(input('请输入一个整数'))
    b=int(input('请输入一个整数'))
    result=a/b
except BaseException as e:
    print('出错了')
    print(e)
else:
    print('计算结果为：',result)
finally:
    print('sj')
print('程序结束')
"""

