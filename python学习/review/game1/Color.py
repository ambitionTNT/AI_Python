# python learing
# author:TNT
from random import randint


class Color(object):
    RED = (255, 0, 0)
    GREED = (0, 255, 0)
    BULL = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获取随机颜色"""
        r = randint(0,255)
        b = randint(0,255)
        g = randint(0,255)
        return (r, g, b)

