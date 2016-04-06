# Findtrip说明文档

## 介绍
Findtrip是一个基于Scrapy的机票爬虫，目前整合了国内两大机票网站（去哪儿 + 携程）

## Introduction
Findtrip is a webspider for flight tickets by Scrapy, it contain two website of china Qua & Ctrip


##安装
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

