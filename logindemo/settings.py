
# -*- coding: utf-8 -*-

BOT_NAME = 'logindemo'

SPIDER_MODULES = ['logindemo.spiders']
NEWSPIDER_MODULE = 'logindemo.spiders'


ROBOTSTXT_OBEY = True


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 543,
}

ITEM_PIPELINES = {'logindemo.pipelines.MyImageDownloadPipeLine': 1}

IMAGES_STORE = '/Users/chenglp/Program/scrapy_pro/example/logindemo/image'


COOKIES_DEBUG = True
COOKIES_ENABLED = True
