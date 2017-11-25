from django.db import models


class Product(models.Model):
    site_product_id = models.PositiveIntegerField()
    name = models.TextField()
    brand = models.TextField()
    categories = models.TextField()
    description = models.TextField()
    material = models.TextField()
    made_in = models.TextField()
    url = models.URLField()
    site = models.URLField()

    def __str__(self):
        return self.name


class Image(models.Model):
    url = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
