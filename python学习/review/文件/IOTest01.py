# python learing
# author:TNT
def main():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('未找到指定文件')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('解码错误')
    finally:
        if f:
            f.close()





if __name__ == '__main__':
    main()