# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from findtrip.spiders.washctrip import wash

class CtripPipeline(object):
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
