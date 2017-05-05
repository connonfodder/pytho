# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
import hashlib

class MyImagesPipeline(ImagesPipeline):
    '''
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)
    '''

    def item_completed(self, results, item, info):
        filename = 'age_' + item['age'] +'_price_'+ item['price'] + '.html'
        strs = '<h3>年龄:%s</h3>' \
                '<h3>素质:%s</h3>' \
                '<h3>项目:%s</h3>' \
                '<h3>价格:%s</h3>' \
                '<h3>身材:%s</h3>' \
                '<h3>环境:%s</h3>' \
                '<h3>安全:%s</h3>' %(item['age'],item['quality'],item['project'],item['price'],item['shape'],item['env'],item['security'])
        index = 0
        for img in item['image_urls']:
            hash_str = (hashlib.sha1(img).hexdigest(),)
            strs = strs + '<a href="img/full/' + hash_str + '.jpg">图片' + index + '</a>'
            index = index + 1
                
        with open(filename, 'wb') as f:
            f.write(strs)
        return item
        '''
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_urls'] = image_paths
        return item
        '''
		
