# coding=utf-8
from scrapy.spiders import CrawlSpider, Spider
from imagedemo.items import MyItem
from scrapy.shell import inspect_response


class ImageSpider(Spider):
    name = 'hlhua'
    start_urls = ['http://www.hlhua.com/']

    def parse(self, response):
        # inspect_response(response, self)
        images = []
        for each in response.xpath("//img[@class='goodsimg']/@src").extract():

            m = MyItem()
            m['image_urls'] = [each,]
            images.append(m)
        return images
