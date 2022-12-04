# python learing
# author:TNT
from PIL import Image, ImageFilter

image = Image.open('../../ python进阶之路/第九章 并发编程/thumbnails/guido.jpg')
image.filter(ImageFilter.CONTOUR).show()