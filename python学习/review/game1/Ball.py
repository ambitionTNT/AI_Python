# python learing
# author:TNT
from math import sqrt

import pygame

from review.game1.Color import Color


class Ball(object):
    """球类"""
    def __init__(self, x, y, radius, sx, sy, color = Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():

            self.sy = -self.sy

    def eat(self,other):
        """吃其他球类"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.y, self.y - other.y
            distant = sqrt(dx ** 2 + dy ** 2)

            if distant <self.radius + other.radius and\
                self.radius > other.radius:
                other.alive = False
                self.radius += int(other.radius * 0.416)
    def draw(self,screen):
        """在窗口上绘制小球"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)


