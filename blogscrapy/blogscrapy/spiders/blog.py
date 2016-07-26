# coding=utf-8
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import Request, CrawlSpider, Rule
from blogscrapy.items import BlogScrapyItem

class WendaSpider(CrawlSpider):
    # 爬虫唯一标示
    name = 'oschina'

    # 允许的domain
    allowed_domains = ['oschina.net']

    # 种子url
    start_urls = [
        'http://www.oschina.net/blog',
    ]

    rules = (
        # 解析博客详情url地址callback到parse_page, follow为false, 则url不会跟进爬取了
        Rule(LinkExtractor(allow=('my\.oschina\.net/.+/blog/\d+$',)), callback='parse_page',
             follow=False,),
    )

    # 博客详情页面解析
    def parse_page(self, response):
        loader = ItemLoader(BlogScrapyItem(), response=response)
        loader.add_xpath('title', "//div[@class='title']/text()")
        loader.add_xpath('content', "//div[@class='BlogContent']")
        loader.add_value('url', response.url)
        return loader.load_item()

