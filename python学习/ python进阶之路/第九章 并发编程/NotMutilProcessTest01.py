# python learing
# author:TNT

from time import time

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5

def is_prime(n):
    """判断是否为素数"""
    for factor in range(2, int(n**0.5)+1):
        if n % factor == 0:
            return False

    return True


def main():
    start = time()
    for number in PRIMES:
        isprime=  is_prime(number)
        print('%d is prime : %s' %(number, isprime))
    end = time()
    print('总共消费了%.3f秒' %(end - start))

if __name__ == '__main__':
    main()







