# python learing
# author:TNT
"""异步IO"""

import asyncio
def num_generator(m, n):
    """指定范围的数字生成器"""
    yield from range(m, n + 1)








'''函数前面加上 async 关键字，就变成了 async 函数。这种函数最大特点是执行可以暂停，交出执行权。'''
async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break

        if flag:
            print('Prime=>', i)
            primes.append(i)

        await asyncio.sleep(0.001)

    return tuple(primes)

async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square => ', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares

def main():
    """主函数"""
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()



if __name__ == '__main__':
    main()