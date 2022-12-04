# python learing
# author:TNT
from functools import wraps



def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")


hi()





'''将函数作为参数传给另一个函数'''


def hi2():
    return "hi yasoob!"


def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

print("----------")
doSomethingBeforeHi(hi2)


'''装饰器让你在一个函数的前后去执行代码。'''

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

print("*****************************")
a_function_requiring_decoration()

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
print("*****************************")
a_function_requiring_decoration()



print("--------------------------------------------------------------------------------------------------")


@a_new_decorator
def a_function_requiring_decoration2():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to remove my foul smell")
print("--------------------------------------------------------------------------------------------------")

a_function_requiring_decoration2()


print(a_function_requiring_decoration2.__name__)

