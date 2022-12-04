# python learing
# author:TNT
'''
map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
'''
## 使用 lambda 匿名函数
items1 = list(map(lambda x: x**2, filter(lambda x: x % 2, range(1, 10))))
print(items1)

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

items2 = [x ** 2 for x in range(1, 10) if x % 2]
print(items2)
