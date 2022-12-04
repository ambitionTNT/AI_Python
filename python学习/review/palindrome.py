# python learing
# author:TNT
#实现判断一个数是不是回文数的函数。

def is_palindrome(x):
    tatol = x
    factor = 0
    if(x < 0 or x % 10 == 0):
        return False
    while (tatol > 0):
        ##获取最末位上的数字，重新得到新的数
        factor = factor * 10 + tatol % 10
        tatol = tatol //10
    if(x == factor):
        return True
    else:
        return False
if __name__ == '__main__':
    print(is_palindrome(1234321))
    print(is_palindrome(12345))


