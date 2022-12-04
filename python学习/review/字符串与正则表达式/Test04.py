# python learing
# author:TNT
import re
def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡.'
    setence_list = re.split(r'[，。,.]',poem)
    print(setence_list)
    while '' in setence_list:
        setence_list.remove('')
    print(setence_list)
if __name__ == '__main__':
    main()