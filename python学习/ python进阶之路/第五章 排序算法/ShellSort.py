# python learing
# author:TNT

'''by Donald Shell
    定义一个增量血猎Dn>Dn-1>...D1 = 1
    希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。

    希尔排序的基本思想是：
        先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。
    对每个增量Dk进行Dk-间隔的 排序
    原始算法 Dn = 【N/2】...

'''

def shell_Sort(arr, comp=lambda x, y: x > y):
    '''希尔排序'''
    length = len(arr)
    D = int(length / 2)
    while D > 0:
        for p in range(D, length):
            temp = arr[p]
            # for i in range(p, -1, -D):
            #     if arr[i-D] > temp:
            #         arr[i] = arr[i-D]
            #     else:
            #         break
            # arr[i] = temp

            i = p
            while i > 0 and arr[i-D] > temp:
                arr[i] = arr[i-D]
                i -= D
            arr[i] = temp

        D = int(D/2)

    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(shell_Sort(arr))


