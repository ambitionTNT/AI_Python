# python learing
# author:TNT


'''下面的代码异步的从5个URL中获取页面并通过题: async with session
'''
import asyncio
import re

import aiohttp as aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')



async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()

async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))


def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    cos = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(cos))
    loop.close()

if __name__ == '__main__':
    main()