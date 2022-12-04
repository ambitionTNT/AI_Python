''# python learing
# author:TNT

import json
def main():
    mydict = {
        "name": "张传龙",
        "age": 23,
        "qq": 1292217724,
        "friends": ["袁诗淇", "胡乐天"],
        "cars": [
            {"brand": "BYD", "max_speed": 180},
            {"brand": "Audi", "max_speed": 280},
            {"brand": "Benz", "max_speed": 320}
        ]
    }


    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('数据保存成功')


'''
json模块主要有四个比较重要的函数，分别是：

dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
'''

if __name__ == '__main__':
    main()