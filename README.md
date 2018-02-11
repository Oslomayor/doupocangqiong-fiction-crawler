# doupocangqiong-fiction-crawler
爬取《斗破苍穹》小说全文

网址：[斗破苍穹](http://www.doupoxs.com/doupocangqiong/)

#### 6:29 PM, Feb 11th, 2018 @ home Shangyu

### 原理说明

1. Python 爬虫， 爬取《斗破苍穹》小说的全文

2. 手动浏览，找到每一章节的 url 规律

   > 第1章 http://www.doupoxs.com/doupocangqiong/2.html
   > 第2章 http://www.doupoxs.com/doupocangqiong/5.html
   > 第3章 http://www.doupoxs.com/doupocangqiong/6.html
   > 第4章 http://www.doupoxs.com/doupocangqiong/7.html
   >  ...
   > 第1623章 http://www.doupoxs.com/doupocangqiong/1664.html
   > 最后一章 http://www.doupoxs.com/doupocangqiong/1665.html
   >

   共 1600多 个页面, 除了第一个页面, 其余的 url 有规律

3. 用列表推倒式生成 url 列表

   ```python
       urls = ['http://www.doupoxs.com/doupocangqiong/{page}.html'\
               .format(page=page) for page in range(2, 1666)]

   ```

4. 用 Chrom 浏览器，观察发现，小说的文字都在 <xmp><p>...</p></xmp> 标签中

   ![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/%E6%96%97%E7%A0%B4%E8%8B%8D%E7%A9%B9.PNG?raw=true)

   使用正则表达式提取

   ```python
   texts = re.findall('<p>(.*?)</p>', res.content.decode('utf-8'))

   ```

5. 运用 Python 的文件操作，保存爬取的信息为 .txt 文件


### 使用说明

1. 源码见 [doupocangqiong-fiction-crawler.py](https://github.com/Oslomayor/doupocangqiong-fiction-crawler/blob/master/doupocangqiong-fiction-crawler.py)
2. 爬取的小说全文见 [斗破苍穹全文](https://github.com/Oslomayor/doupocangqiong-fiction-crawler/blob/master/doupocangqiong-fiction.txt) ，14.8 MB , 有点大， github 不能直接显示
