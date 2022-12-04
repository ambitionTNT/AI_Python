# python learing
# author:TNT

#写一个程序判断输入的正整数是不是回文素数。
from review.is_Prime import is_Prime
from review.palindrome import is_palindrome

if __name__ == '__main__':
    num = int(input("请输入一个整数："))
    if is_Prime(num) and is_palindrome:
        print("是回文质数")
    else:
        print("不是回文质数")

