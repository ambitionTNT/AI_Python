# python learing
# author:TNT
from math import sqrt
#定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
class Point(object):
    def __init__(self,x=0,y=0):
        '''初始化方法
        :param x:横坐标
        :param y :纵坐标
        '''
        self.x = x
        self.y = y

    def move_to(self,dx,dy):
        """移动到指定位置


        """
        self.x = dx
        self.y = dy
    def move_by(self,dx,dy):
        '''
        :param dx:x轴移动的单位数
        :param dy:y轴移动的单位数
        :return: 无返回
        '''
        self.x += dx
        self.y += dy
    def distance_to(self,other):
        return sqrt(
            (self.x - other.x) ** 2 + (self.y -other.y) ** 2
        )

    def __str__(self):
        return '(%s,%s) ' %(str(self.x),str(self.y))

def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
