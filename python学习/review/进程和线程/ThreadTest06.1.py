# python learing
# author:TNT
'''在上面的代码中，我故意先去创建了一个列表容器然后填入了100000000个数，
这一步其实是比较耗时间的，所以为了公平起见，当我们将这个任务分解到8个进程中去执行的时候，
我们暂时也不考虑列表切片操作花费的时间，只是把做运算和合并运算结果的时间统计出来，代码如下所示。'''
from multiprocessing import Process, Queue


from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for num in curr_list:
        total += num
    result_queue.put(total)


def main():
    processes = []
    # 创建一个数据集
    number_list = [x for x in range(1, 100000001)]

    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算

    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index+12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()

    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time :', (end - start), 's', sep='')




if __name__ == '__main__':
    main()