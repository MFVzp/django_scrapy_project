# coding: utf-8
from datetime import date

import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy_project.items import ProductItem, PriceItem


class MytheresaSpider(RedisSpider):
    name = 'mytheresa'

    def parse(self, response):
        if 'clothing' in response.url:
            common_types = response.xpath('//div[@class="block-content"]/ul/li/a')
        else:
            common_types = response.xpath('//div[@class="block-content"]/ul/li[position()>1]/a')
        for common_type in common_types[:1]:
            common_type_url = common_type.xpath('@href').extract_first('')
            common_type_name = common_type.xpath('text()').extract_first('').strip()
            if response.meta.get('categories'):
                meta = response.meta['categories']
                meta.append(common_type_name)
            else:
                meta = {
                    'categories': [common_type_name, ],
                }
            yield scrapy.Request(
                url=common_type_url,
                callback=self.get_types,
                meta=meta,
                dont_filter=True
            )

    def get_types(self, response):
        types = response.xpath('//ul[@class="level3"]/li')
        url = response.url
        if types:
            for cloth_type in types[:1]:
                url = cloth_type.xpath('a/@href').extract_first('')
                type_name = cloth_type.xpath('a/span[2]/text()').extract_first('').strip()
                response.meta['categories'].append(type_name)
        yield scrapy.Request(
            url=url,
            callback=self.get_items,
            meta={
                'categories': response.meta['categories'],
            }
        )

    def get_items(self, response):
        next_page = response.xpath('//div[@class="pages"]/ul/li[class="next"]')
        if next_page:
            yield scrapy.Request(
                url=next_page.xpath('a/@href'),
                callback=self.get_items,
                meta={
                    'categories': response.meta['categories'],
                }
            )
        items = response.xpath(
            '//div[@class="category-products"]/ul/li[contains(@class,"item")]'
        )
        for item in items[:1]:
            item = item.xpath('div[@class="product-info"]/h2[@class="product-name"]/a')
            item_url = item.xpath('@href').extract_first('')
            item_name = item.xpath('text()').extract_first('')
            response.meta['categories'].append(item_name)
            yield scrapy.Request(
                url=item_url,
                callback=self.get_item,
                meta={
                    'categories': response.meta['categories'],
                }
            )

    def get_item(self, response):
        product = ProductItem()
        price = PriceItem()
        product['site_product_id'] = price['site_product_id'] = int(response.xpath(
            '//input[@name="product"]/@value'
        ).extract_first('').strip())

        product['name'] = response.xpath(
            '//div[@class="product-name"]/span/text()'
        ).extract_first('').strip()
        product['brand'] = response.xpath(
            '//div[@class="product-designer"]/span/a/text()'
        ).extract_first('').strip()
        product['categories'] = ' > '.join(response.meta['categories'])
        product['description'] = response.xpath(
            '//p[@class="pa1 product-description"]/text()'
        ).extract_first('').strip()
        product['material'] = response.xpath(
            '//ul[@class="disc featurepoints"]/li[contains(text(), "material")]/text()'
        ).re_first(r'material: (.*)')
        product['made_in'] = response.xpath(
            '//ul[@class="disc featurepoints"]/li[contains(text(), "Made in")]/text()'
        ).re_first(r'Made in (.*)')
        product['url'] = response.url
        product['images'] = response.xpath(
            '//img[@class="gallery-image"]/@src'
        ).extract()
        product['site'] = 'https://www.mytheresa.com/en-us/'
        yield product

        price['date'] = date.today()
        price['currency'] = 'USD'
        price['stock_level'] = response.xpath(
            '//div[@class="product-sku"]/span/text()'
        ).extract_first('').strip()
        price['params'] = {
            'price': float(response.xpath(
                '//div[@class="price-info"]/div/span/span/text()'
            ).re_first(r'\$ (\d*)')),
            'size': response.xpath('//ul[@class="sizes"]/li/a/text()').re(r'(\w+ / US \w+)'),
        }
        yield price
