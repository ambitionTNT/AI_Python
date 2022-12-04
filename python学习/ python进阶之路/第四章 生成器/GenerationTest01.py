# python learing
# author:TNT
"""
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？

如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

"""


#生成式
L = [x * x for x in range(10)]
print(L)
#生成器
g = (x * x for x in range(10))
print(g)
'''可以通过next()函数获得generator的下一个返回值：'''

for x in g:
    print(x)

def fib(max):
    num, first, second = 0, 0, 1
    while num < max:
        print(second)
        first, second = second, first +second
        num += 1
    return 'done'

fib(10)
'''仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator函数，只需要把print(b)改为yield b就可以了：'''


def fib2(max):
    num, first, second = 0, 0, 1
    while num < max:
        yield second
        first, second = second, first + second
        num += 1
    return 'done'


