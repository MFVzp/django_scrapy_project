# -*- coding: utf-8 -*-
from .items import PriceItem, ProductItem
from spiders_app.tasks import add_product, add_price


class ScrapyProjectPipeline(object):

    def __init__(self):
        self.product_store = list()
        self.price_store = list()

    def save_items(self):
        add_product.delay(
            [dict(product) for product in self.product_store]
        )
        self.product_store.clear()
        add_price.delay(
            [dict(price) for price in self.price_store]
        )
        self.price_store.clear()

    def process_item(self, item, spider):
        print(item)
        if isinstance(item, ProductItem):
            self.product_store.append(item)
        elif isinstance(item, PriceItem):
            self.price_store.append(item)
        #if (len(self.product_store) + len(self.price_store)) > 500:
        self.save_items()

    def close_spider(self, spider):
        (self.product_store or self.price_store) and self.save_items()
