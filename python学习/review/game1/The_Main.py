# python learing
# author:TNT
from random import randint

import pygame

from review.game1.Ball import Ball
from review.game1.Color import Color


def main():
    #定义装球的容器
    balls = []

    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')

    # # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
    # screen.fill((255,255,255))
    # # 通过指定的文件名加载图像
    # ball_image = pygame.image.load('./res/ball.png')
    # # 在窗口上渲染图像
    # screen.blit(ball_image, (50, 50))
    # # # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    # # pygame.draw.circle(screen, (255, 0, 0),(100, 100), 30, 0)
    # # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    # pygame.display.flip()
    running = True
    # 开启一个事件循环处理发生的事件
    # 如果要让上面代码中的小球动起来，可以将小球的位置用变量来表示，并在循环中修改小球的位置再刷新整个窗口即可。
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #处理鼠标事件的代码
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #获取鼠标点处的位置
            x, y = event.pos
            radius = randint(10, 100)
            sx, sy = randint(-10, 10), randint(-10, 10)
            color = Color.random_color()
            # 在点击鼠标的位置创建一个球(大小、速度和颜色随机)
            ball = Ball(x, y, radius,sx, sy, color)
            #将球加入到容器中
            balls.append(ball)
        screen.fill((255, 255, 255))
        for ball in balls :
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)


        # ball_image = pygame.image.load('./res/ball.png')
        # # 在窗口上渲染图像
        # screen.blit(ball_image, (x, y))
        #pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
        # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其他的球
            for other in balls:
                ball.eat(other)

if __name__ == '__main__':
    main()

