# python learing
# author:TNT
from math import sqrt

def is_Prime(num):
    '''判断是否为素数'''

    if num <= 1:
        return False

    for factor in range(2,int(sqrt(num))+1):
        if num % factor == 0:
            return False

    return True
def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1,10000):
            if is_Prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) +'\n')
    except IOError as ex :
        print(ex)
        print('写文件时发生错误！')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')

if __name__ == '__main__':
    main()
