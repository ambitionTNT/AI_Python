# python learing
# author:TNT


def calc_ava():
    '''流式计算平均值'''
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter

