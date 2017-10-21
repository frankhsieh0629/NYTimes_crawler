# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NytimesCrawlerItem(scrapy.Item):
    story_title = scrapy.Field()
    story_link = scrapy.Field()
    story_content = scrapy.Field()
    # name = scrapy.Field()
    pass
