# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

class SpiderTest(scrapy.Spider):
    name = "test"
    #allowed_domains = ["xicidaili.com"]
    start_urls = [
        #"https://shouji.suning.com/phone2018.html"
        'https://list.suning.com/0-20006-0-0-0-0-0-0-0-0-4245046.html?safp=d488778a.phone2018.103327226421.2&safc=cate.0.0'
    ]

    def parse(self, response):
        print('--------------------')
        selector = Selector(response)

        # "https://shouji.suning.com/phone2018.html"
        # e = selector.xpath('//a[text()="Apple"]')
        # print(e.xpath('@href').extract()[0])

        ss = selector.xpath('//li[@doctype="1" and @ishwg=""]')
        for s in ss:
            id = s.xpath('@id').extract()[0].split('-')
            print('https://product.suning.com/{}/{}.html'.format(id[0], id[1]))



        print('--------------------')


