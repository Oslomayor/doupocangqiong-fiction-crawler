# 4:24 PM, Feb 11, 2018 @ home, Shangyu
# 不依赖 BeautifulSoup 库, 用正则表达式和re模块提取文本
# 爬取《斗破苍穹》小说全文
# http://www.doupoxs.com/doupocangqiong/

# urls:
# http://www.doupoxs.com/doupocangqiong/2.html
# http://www.doupoxs.com/doupocangqiong/5.html
# http://www.doupoxs.com/doupocangqiong/6.html
# http://www.doupoxs.com/doupocangqiong/7.html
# ...
# http://www.doupoxs.com/doupocangqiong/1664.html
# http://www.doupoxs.com/doupocangqiong/1665.html
# 共 1662 个页面, 除了第一个页面, 其余的 url 有规律

import re
import requests
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
file = open(r'E:\AllPrj\PyCharmPrj\py-crawler\doupocangqiong-fiction\doupocangqiong-fiction.txt', 'a+', encoding='utf-8')

def get_info(url):
    print('on page:' + url)
    res = requests.get(url, headers=headers)
    # 网页返回代码 200 代表请求成功
    if res.status_code == 200:
        # Python 的解码和编码不是很理解，比如这里的 content.decode
        texts = re.findall('<p>(.*?)</p>', res.content.decode('utf-8'))
        for text in texts:
            # 在正则表达式中加上 [;] , 表达式不工作，无法过滤 '&ldquo;' '&hellip' 这些不需要的字符串
            # text = re.sub('[;][&][a-z]+', '', text).strip('.;')
            text = re.sub('[&][a-z]+', '', text).strip('.;')
            print(text)
            file.write(text + '\n')
    print('this page finished')
    print('\n\n')

def main():
    urls = ['http://www.doupoxs.com/doupocangqiong/{page}.html'.format(page=page) for page in range(2, 1666)]
    for url in urls:
        get_info(url)
        time.sleep(1)
    file.close()
if __name__ == '__main__':
    main()
