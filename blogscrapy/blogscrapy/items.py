# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from w3lib.html import remove_tags


def filter_title(value):
    return value.strip()


class BlogScrapyItem(scrapy.Item):
    title = scrapy.Field(input_processor=MapCompose(remove_tags, filter_title))
    content = scrapy.Field(input_processor=MapCompose(remove_tags, filter_title))
    url = scrapy.Field(input_processor=MapCompose(remove_tags, filter_title))



