# python learing
# author:TNT

from PIL import Image


image = open('./res/luohao.png')
for x in range(80, 310):
    for y in range(20, 360):
        image.putpixel((x, y), (128, 128, 128))

image.show()