# python learing
# author:TNT
'''
插入排序，既把第n个元素插入到前n-1的已经排好序的数组中
使用一下 lambad表达式
1、算法从 第二个元素开始，因为第一个元素已经有序
    最坏,逆序：O(n^2)
    最好,顺序 O(n)
    是一个稳定的算法
2、排序的目的就是减少逆序对，冒泡类似，交换一次就是为了消除逆序对
'''


def insertSort(items, comp=lambda x, y: x > y):
    length = len(items)
    for p in range(1, length):
        #拿到下一个元素
        Tmp = items[p]
        i = p
        while i > 0 and items[i-1] > Tmp:
            items[i] = items[i-1]
            i -= 1

        items[i] = Tmp
    return items

arr = [64, 34, 25, 12, 22, 11, 90]
print(insertSort(arr))

