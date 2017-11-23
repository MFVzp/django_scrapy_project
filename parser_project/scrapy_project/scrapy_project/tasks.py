# -*- coding: utf-8 -*-
from celery import Celery
from pymongo import MongoClient


app = Celery('sc_test', broker='amqp://ilya:intel@localhost:5672/myvhost')
db = MongoClient('localhost', port=27017)
db = db['mytheresa_db']


@app.task(name='add_product_item')
def add_product_item(item):
    db.product_items.insert_one(item)


@app.task(name='add_price_item')
def add_price_item(item):
    db.price_items.insert_one(item)
