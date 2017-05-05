from scrapy import cmdline

cmdline.execute("scrapy crawl pronlol -o items.json".split())