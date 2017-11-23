# -*- coding: utf-8 -*-
import scrapy


class ProductItem(scrapy.Item):
    site_product_id = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    categories = scrapy.Field()
    description = scrapy.Field()
    material = scrapy.Field()
    made_in = scrapy.Field()
    url = scrapy.Field()
    images = scrapy.Field()
    site = scrapy.Field()


class PriceItem(scrapy.Item):
    site_product_id = scrapy.Field()
    params = scrapy.Field()
    stock_level = scrapy.Field()
    currency = scrapy.Field()
    date = scrapy.Field()
