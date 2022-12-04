# python learing
# author:TNT
from PIL import Image

image1 = Image.open('../../ python进阶之路/第九章 并发编程/thumbnails/guido.jpg')
image1.rotate(180).show()
image1.transpose(Image.FLIP_LEFT_RIGHT).show()