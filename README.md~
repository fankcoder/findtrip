# Findtrip说明文档

## 介绍
Findtrip是一个基于Scrapy的机票爬虫，目前整合了国内两大机票网站（去哪儿 + 携程）

## Introduction
Findtrip is a webspider for flight tickets by Scrapy,which contains two major china ticket websites ---- Qua & Ctrip


## 安装
在用户目录下执行,将代码clone到本地
```
git clone https://github.com/fankcoder/findtrip.git
```

所需运行环境,请看 django-todolist/doc/requirements.txt

本程序使用selenium+ phantomjs模拟浏览器行为获取数据，phantomjs浏览器下载地址（当然使用Firefox也可以，不过打开速度就会慢很多）

http://npm.taobao.org/dist/phantomjs



数据库使用Mongodb存储，运行需要安装Mongodb，安装传送门

https://www.mongodb.org/downloads

如果仅仅作为测试不需要使用Mongodb，可以注释settings.py下对应行
```
'''
ITEM_PIPELINES = {
    'findtrip.pipelines.MongoDBPipeline': 300,
}

MONGODB_HOST = 'localhost' # Change in prod
MONGODB_PORT = 27017 # Change in prod
MONGODB_DATABASE = "findtrip" # Change in prod
MONGODB_COLLECTION = "qua"
MONGODB_USERNAME = "" # Change in prod
MONGODB_PASSWORD = "" # Change in prod
'''

```

## 运行
以下命令统一运行在findtrip/目录下，与scrapy.cfg文件同级目录

去哪儿网单爬，终端输入
```
scrapy crawl Qua
```
携程网单爬，终端输入
```
scrapy crawl Ctrip
```
去哪儿，携程多爬，同时爬取，终端输入
```
scrapy crawlall
```

## 部分json数据
去哪儿网
```
[{"airports": ["NAY", "Nanyuan", "XMN", "Xiamen"], "company": ["China", "KN5927(73S)"], "site": "Qua", "flight_time": ["4:00", "PM", "7:00", "PM"], "passtime": ["3h"], "price": ["\u00a5", "689"]},
{"airports": ["PEK", "Beijing", "RIZ", "Rizhao", "RIZ", "Rizhao", "XMN", "Xiamen"], "company": ["Shandong", "SC4678(738)", "Same", "Shandong", "SC4678(738)"], "site": "Qua", "flight_time": ["3:20", "PM", "4:50", "PM", "45m", "5:35", "PM", "8:05", "PM"], "passtime": ["1h30m", "2h30m"], "price": ["\u00a5", "712"]},...]

```
携程网
```
[{"flight_time": [["10:30", "20:50"], ["12:15", "22:20"]], "price": ["\u00a5", "580"], "airports": [["\u9ad8\u5d0e\u56fd\u9645\u673a\u573aT4", "\u5357\u4eac\u7984\u53e3\u56fd\u9645\u673a\u573aT2"], ["\u5357\u4eac\u7984\u53e3\u56fd\u9645\u673a\u573aT2", "\u9996\u90fd\u56fd\u9645\u673a\u573aT2"]], "company": ["\u4e1c\u65b9\u822a\u7a7a", "MU2891", "\u4e1c\u65b9\u822a\u7a7a", "MU728"], "site": "Ctrip"},
{"flight_time": [["11:05", "17:55"], ["12:50", "19:50"]], "price": ["\u00a5", "610"], "airports": [["\u9ad8\u5d0e\u56fd\u9645\u673a\u573aT4", "\u5408\u80a5\u65b0\u6865\u56fd\u9645\u673a\u573a"], ["\u5408\u80a5\u65b0\u6865\u56fd\u9645\u673a\u573a", "\u9996\u90fd\u56fd\u9645\u673a\u573aT2"]], "company": ["\u4e1c\u65b9\u822a\u7a7a", "MU5169", "\u4e1c\u65b9\u822a\u7a7a", "MU5171"], "site": "Ctrip"},...]
```
