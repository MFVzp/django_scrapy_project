# -*- coding: utf-8 -*-
from celery.task import task

from .models import Product, Image


@task(name='add_product')
def add_product(item_list):
    for item in item_list:
        print(item)
        product, created = Product.objects.get_or_create(
            site_product_id=item.get('site_product_id'),
            name=item.get('name'),
            brand=item.get('brand'),
            categories=item.get('categories'),
            description=item.get('description'),
            material=item.get('material') or '',
            made_in=item.get('made_in') or '',
            url=item.get('url'),
            site=item.get('site')
        )
        print(product, created)
        if created:
            for url in item.get('images', []):
                Image(
                    url=url,
                    product=product
                )


@task(name='add_price')
def add_price(item_list):
    pass
