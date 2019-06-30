# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class NCfulltext_item(Item):
    _id = Field()
    url = Field()
    title = Field()
    authors = Field()
    abstract = Field()
    results = Field()
    discussion = Field()
    methods = Field()
    references = Field()
    introduction = Field()