import sys
import scrapy
import logging
from scrapy.selector import Selector
from scrapy.http import Request
from pronlol.items import PronlolItem
reload(sys)   
sys.setdefaultencoding('utf-8')
baseurl = 'http://www.1dav.com/'
class DmozSpider(scrapy.Spider):
    name = "pronlol"
    allowed_domains = ["1dav.com"]
    start_urls = [
        'http://www.1dav.com/class.php?cid=79&page=1',
        'http://www.1dav.com/class.php?cid=79&page=2',
        'http://www.1dav.com/class.php?cid=79&page=3',
        'http://www.1dav.com/class.php?cid=79&page=4',
        'http://www.1dav.com/class.php?cid=79&page=5',
        'http://www.1dav.com/class.php?cid=29&page=1',
        'http://www.1dav.com/class.php?cid=29&page=2',
        'http://www.1dav.com/class.php?cid=29&page=3',
        'http://www.1dav.com/class.php?cid=29&page=4',
        'http://www.1dav.com/class.php?cid=29&page=5',
        'http://www.1dav.com/class.php?cid=115&page=1',
        'http://www.1dav.com/class.php?cid=115&page=2',
        'http://www.1dav.com/class.php?cid=115&page=3',
        'http://www.1dav.com/class.php?cid=115&page=4',
        'http://www.1dav.com/class.php?cid=115&page=5',
        'http://www.1dav.com/class.php?cid=115&page=6',
        'http://www.1dav.com/class.php?cid=115&page=7',
        'http://www.1dav.com/class.php?cid=115&page=8',
        'http://www.1dav.com/class.php?cid=115&page=9',
        'http://www.1dav.com/class.php?cid=115&page=10',
        'http://www.1dav.com/class.php?cid=115&page=11',
        'http://www.1dav.com/class.php?cid=115&page=12',
        'http://www.1dav.com/class.php?cid=115&page=13',
        'http://www.1dav.com/class.php?cid=115&page=14',
        'http://www.1dav.com/class.php?cid=115&page=15'
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
        links = selector.xpath('//*[@id="video-6638"]/div')
        print('the lenth of links: %s' %len(links))
        for link in links:
            url = baseurl + link.xpath('a/@href')[0].extract()
            print url
            yield Request(url = url, callback= self.parse_item)

    def parse_item(self, response):
        print response
        selector = Selector(response)
        title = response.xpath('//*[@id="video"]/h1/text()').extract()
        videolink = response.xpath('//*[@id="video"]/div[1]/div[2]/a[1]/@href').extract()
        playcount = response.xpath('/html/body/div[5]/div/div[2]/strong/text()').extract()
        tags = response.xpath('//a[contains(@href, "search.php?action=search")]/text()').extract()
        item = PronlolItem()
        print('title:%s videolink:%s playcount:%s tags:%s' %(title, videolink, playcount,tags))
        item['title'] = title
        item['videolink'] = videolink
        item['playcount'] = '0'
        item['tags'] = ' - '
        yield item
