# python learing
# author:TNT
from PIL import Image
image = Image.open('./res/img.png')

image.format('PNG')
image.size(500, 750)
image.mode('RGB')

image.show()