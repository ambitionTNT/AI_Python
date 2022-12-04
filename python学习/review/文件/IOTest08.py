# python learing
# author:TNT
import requests
import json


def main():
    APIKey='8289b63d8ced369e776890eb29032ced'
    resp = requests.get('http://api.tianapi.com/guonei/?key='+APIKey+'&num=10')
    data_model = json.loads(resp.text)
    print(data_model)
    print(type(data_model['newslist']))
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()