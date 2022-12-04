# python learing
# author:TNT
from  math import sqrt
def is_Prime(num):
    for factor in range(2,int(num ** 0.5) +1):
        if num % factor  == 0:
            return False

    return True


if __name__ == '__main__':
    print(is_Prime(2))
    print(is_Prime(13))
    print(is_Prime(1))


