# python learing
# author:TNT
"""
冒泡排序:
    顾名思义
    最坏,逆序：O(n^2)
    最好,顺序 O(n)
    是一个稳定的算法

"""
def bubble_Sort(items):
    #计算长度
    length = len(items)
    #外层循环用于控制需要几次冒泡
    for i in range(length-1):
        #内层控制每个元素的冒泡
        #一趟排序
        flag = False
        #进行剪枝
        for j in range(length - i-1):
            if items[j] > items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
                flag = True
                #items[j],items[j+1] = items[j+1],items[j]
        #全程无交换的情况
        if not flag:
            break


    return items

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_Sort(arr))