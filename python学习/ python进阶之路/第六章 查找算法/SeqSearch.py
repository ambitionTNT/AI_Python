# python learing
# author:TNT


def SeqSearch(items, key):
    '''
    顺序查找
    :param items:数据集
    :param key: 查找关键字
    :return: 元素的位置
    '''
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1