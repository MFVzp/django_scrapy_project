from django.db import models


class Product(models.Model):
    site_product_id = models.PositiveIntegerField()
    name = models.TextField()
    brand = models.TextField()
    categories = models.TextField()
    description = models.TextField()
    material = models.TextField(blank=True)
    made_in = models.TextField(blank=True)
    url = models.URLField()
    site = models.URLField()


class Image(models.Model):
    url = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
