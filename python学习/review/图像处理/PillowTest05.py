# python learing
# author:TNT
from PIL import Image

image1 = Image.open('./res/luohao.png')
image2 = Image.open('../../ python进阶之路/第九章 并发编程/thumbnails/guido.jpg')
rect = 80, 20, 310, 360
guido_Head = image2.crop(rect)
width, height = guido_Head.size
image1.paste(guido_Head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
image1.show()
