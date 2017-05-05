import sys
import scrapy
import logging
import datetime
import hashlib
from scrapy.selector import Selector
from scrapy.http import Request
from tutorial.items import DmozItem
reload(sys)   
sys.setdefaultencoding('utf-8')
baseurl = 'http://www.missweike2017.com'
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["missweike2017.com"]
    start_urls = [
        'http://www.missweike2017.com/class.asp?page=1&typeid=4&areaid=301',
        'http://www.missweike2017.com/class.asp?page=2&typeid=4&areaid=301',
        'http://www.missweike2017.com/class.asp?page=3&typeid=4&areaid=301'
        ]
    logging.getLogger("requests").setLevel(logging.WARNING)  # 将requests的日志级别设成WARNING
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='cataline.log',
                filemode='w')
    
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback = self.parse_table)
        
    def parse_table(self, response):
        selector = Selector(response)
        trs = selector.xpath('//a[contains(@href, "show.asp")]/../..')
        print(len(trs))
        for tr in trs:
            tds = tr.xpath('td')
            #print(len(tds))
            #print(tr.extract())
            try:
                time = tds[5].xpath('text()')[0].extract()  # 2017/4/25 22:20:28
                now = datetime.datetime.today()
                temp = datetime.datetime.strptime(time, "%Y/%m/%d %H:%M:%S")
                if (now - temp).days < 30:
                    url = baseurl + tds[3].xpath('a/@href')[0].extract()
                    title = tds[3].xpath('a/@title')[0].extract()
                    locs = tds[2].xpath('a/text()')
                    area = locs[0].extract() + locs[1].extract()
                    yield Request(url = url, callback= self.parse_item)
            except IndexError:
                pass

    def parse_item(self, response):
        selector = Selector(response)
        trs = response.xpath('//td[contains(@class, "neirong2")]/font/text()')
        area = '深圳'
        age = trs[2].extract()
        quality = trs[3].extract()
        shape = trs[4].extract()
        project = trs[5].extract()
        price = trs[6].extract()
        env = trs[8].extract()
        security = trs[9].extract()
        args = (area, age, quality, shape, project, price, env, security)
        #print('area:%s age:%s quality:%s shape:%s project:%s price:%s env:%s security:%s' %args)

        imgs = response.xpath('//img[contains(@src, "UploadFile")]/@src').extract()
        imglist = []
        for img in imgs:
            imglist.append(baseurl + img)
            
        item = DmozItem()
        item['age'] = age
        item['quality'] = quality
        item['shape'] = shape
        item['project'] = project
        item['price'] = price
        item['env'] = env
        item['security'] = security
        item['title'] = 'title'
        item['area'] = 'area'
        item['image_urls'] = imglist
        self.write_to_files(item)
        yield item
    
    def write_to_files(self,item):
        print 'ready to write to files...'
        filename = 'age_' + item['age'] +'_price_'+ item['price'] + '.html'
        strs =  '<h3>地区:%s</h3>' \
                '<h3>年龄:%s</h3>' \
                '<h3>素质:%s</h3>' \
                '<h3>项目:%s</h3>' \
                '<h3>价格:%s</h3>' \
                '<h3>身材:%s</h3>' \
                '<h3>环境:%s</h3>' \
                '<h3>安全:%s</h3>' %('广东-深圳', item['age'],item['quality'],item['project'],item['price'],item['shape'],item['env'],item['security'])
        index = 0
        for img in item['image_urls']:
            hash_str = hashlib.sha1(img).hexdigest()
            print hash_str
            strs = '%s <a href="img/full/%s.jpg">pic%d</a>' %(strs, hash_str, index)
            index = index + 1
                
        with open(filename, 'wb') as f:
            f.write(strs)
