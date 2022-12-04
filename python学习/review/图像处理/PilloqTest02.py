# python learing
# author:TNT
from PIL import Image



image = Image.open('./res/img.png')


rect = 80, 20, 310, 360
image.crop(rect).show()