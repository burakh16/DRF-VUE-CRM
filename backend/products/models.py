from django.db import models

from common.models import BaseModel


class ProductManager(models.Manager):
    def available_products(self):
        return self.filter(qty__gt=0)


class Product(BaseModel):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=19)
    qty = models.IntegerField()
    description = models.CharField(max_length=50,default="")

    objects = ProductManager()

    class Meta:
        ordering = ('-created_at',)