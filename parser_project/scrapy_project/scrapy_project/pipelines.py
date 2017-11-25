# -*- coding: utf-8 -*-
from .tasks import add_product_item, add_price_item
from .items import ProductItem, PriceItem


class ScrapyProjectPipeline(object):

    # def __init__(self):
    #     self.store = list()
    #
    # def save_items(self):
    #     for store_item in self.store:
    #         if isinstance(store_item, ProductItem):
    #             add_product_item.delay(dict(store_item))
    #         elif isinstance(store_item, PriceItem):
    #             add_price_item.delay(dict(store_item))
    #     self.store.clear()

    def process_item(self, item, spider):
        # self.store.append(item)
        # if len(self.store) > 100:
        #     self.save_items()
        return item
    #
    # def close_spider(self, spider):
    #     self.store and self.save_items()
