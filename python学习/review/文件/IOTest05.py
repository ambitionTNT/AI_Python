# python learing
# author:TNT
def main():
    try:
        with open('thumb.jpg','rb') as fs1:
            data = fs1.read()
            print(type(data)) # <class 'bytes'>
        with open('正面.jpg','rb') as fs2:
            data = fs2.read()
            print(type(data))
    except FileNotFoundError as ex1:
        print('文件未找到')
    except IOError as e :
        print('读写文件时发生错误')
    print('程序执行结束')


if __name__ == '__main__':
    main()