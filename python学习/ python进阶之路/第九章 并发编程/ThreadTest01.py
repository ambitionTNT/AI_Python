# python learing
# author:TNT
"""
面试题：进程和线程的区别和联系？
进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
线程 - 操作系统分配CPU的基本单位
并发编程（concurrent programming）
1. 提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
2. 改善用户体验 - 让耗时间的操作不会造成程序的假死
"""
import os
from threading import Thread
from glob import glob
'''
生成缩略图
thumbnail函数接受一个元组作为参数，分别对应着缩略图的宽高，在缩略时，
函数会保持图片的宽高比例。如果输入的参数宽高和原图像宽高比不同，则会依据最小对应边进行原比例缩放。
比如:
一张图片为300*420大小的图片
当参数为（200,200）时，生成的缩略图大小为71*100，保持原图的宽高比
'''


try:
    from PIL import Image
except ImportError:
    import Image


PREFIX = 'thumbnails'
def generate_thumbnail(infile, size, format = 'PNG'):
    """生成指定图片文件的缩略图"""
    file, ext = os.path.splitext(infile)
    file = file[file.rfind('/')+1:]
    outfile = f'{PREFIX}\\{file}_{size[0]}_{size[1]}.{ext}'
    #打开这个文件
    img = Image.open(infile)
    #生成缩略图
    img.thumbnail(size, Image.ANTIALIAS)
    #存储这个文件
    img.save(outfile, format)



def main():
    """主函数"""
    # 如果不存在这个文件夹就创建
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
        # glob 用它可以查找符合自己目的的文件,其返回的文件名只包括当前目录里的文件名，不包括子文件夹里的文件
    for infile in glob('images\*.png'):
        for size in (32, 64, 128):
        #创建并启动线程
            Thread(target=generate_thumbnail, args=(infile, (size, size))).start()

if __name__ == '__main__':
	main()

