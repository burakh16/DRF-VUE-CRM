from django.db import models

from common.models import BaseModel


class Customer(BaseModel):

    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500, null=True)
    district = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    tax_office = models.CharField(max_length=50, null=True)
    tax_no = models.CharField(max_length=50, null=True)
    cell_number = models.CharField(max_length=15, null=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name