# python learing
# author:TNT


def binarySearch(items, key):
    """
    折半查找
    :param items:  数据集
    :param key: 待查元素
    :return:
    """
    left, right = 0, len(items)-1
    while left <= right:
        mid  = (left + right) // 2
        if key > items[mid]:
            left = mid + 1
        elif key < items[mid]:
            right = mid -1
        else:
            return mid

    return -1

