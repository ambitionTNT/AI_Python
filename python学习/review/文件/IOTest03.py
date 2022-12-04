# python learing
# author:TNT
import time


def main():
    with open('JDBC课堂笔记.txt', 'r', encoding='gb18030') as f:
        print(f.read())
    # 通过for-in循环逐行读取
    with open('JDBC课堂笔记.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    # 读取文件按行读取到列表中
    with open('JDBC课堂笔记.txt') as f:
        lines = f.readlines()

    print(lines)

if __name__ == '__main__':
    main()