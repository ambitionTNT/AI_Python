# python learing
# author:TNT
#跑马灯
import os
import time
def main():
    content = '北京欢迎您，为你开天辟地...'
    while True:
        #清理屏幕上的内容
        os.system('cls')
        print(content)
        #休眠0.2s
        time.sleep(0.2)
        content = content[1:]+content[0]

if __name__ == '__main__':
    main()