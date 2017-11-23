# -*- coding: utf-8 -*-
from .tasks import add_product_item, add_price_item
from .items import ProductItem, PriceItem
from .settings import NUMBER_OF_ITEMS_TO_INSERT


class ScTestPipeline(object):

    def __init__(self):
        self.store = list()

    def process_item(self, item, spider):
        self.store.append(item)
        if len(self.store) > NUMBER_OF_ITEMS_TO_INSERT:
            for store_item in self.store:
                if isinstance(store_item, ProductItem):
                    add_product_item.delay(dict(store_item))
                elif isinstance(store_item, PriceItem):
                    add_price_item.delay(dict(store_item))
            self.store.clear()
        return item