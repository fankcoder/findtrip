# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from findtrip.spiders.washctrip import wash
import pymongo
from scrapy.conf import settings
from scrapy import log


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DATABASE']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        if item['company']:
            item['company'] = wash(item['company'])
        if item['flight_time']:
            item['flight_time'] = wash(item['flight_time'])
        if item['airports']:
            item['airports'] = wash(item['airports'])
        if item['passtime']:
            item['passtime'] = wash(item['passtime'])
        if item['price']:
            item['price'] = wash(item['price'])        
        for data in item:
            if not data:
                raise DropItem("Missing data!")
        self.collection.insert(dict(item))
        log.msg("Question added to MongoDB database!",
                level=log.DEBUG, spider=spider)

        return item
'''
class QuaPipeline(object):
    def process_item(self, item, spider):
        if item['company']:
            item['company'] = wash(item['company'])
        if item['flight_time']:
            item['flight_time'] = wash(item['flight_time'])
        if item['airports']:
            item['airports'] = wash(item['airports'])
        if item['passtime']:
            item['passtime'] = wash(item['passtime'])
        if item['price']:
            item['price'] = wash(item['price'])
        return item
        '''
