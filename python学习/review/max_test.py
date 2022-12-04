# python learing
# author:TNT
#设计一个函数返回传入的列表中最大和第二大的元素的值.
def max(x):
    list = sorted(x,reverse=True)
    return list[0],list[1]

if __name__ == '__main__':
    list = [7,3,5,7,12,67,33]
    print(max(list))

def max2(x):
    m1, m2 = ([0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def max3(x):
    m1,m2 = (x[0],x[1]) if x[0]> x[1] else (x[1],x[0])
    for index in range(2,len(x)):
        if x[index] >m1:
            m2 = m1
            m1 =x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1,m2

