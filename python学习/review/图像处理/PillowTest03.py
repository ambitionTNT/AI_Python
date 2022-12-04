# python learing
# author:TNT
from PIL import Image

image = Image.open('./res/img.png')
size = 128, 128
image.thumbnail(size)
image.show()