from datetime import date, datetime, timedelta

from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound, ValidationError
from django.db.models import Sum, F, FloatField, Count

from common.models import BaseModel
from customers.models import Customer
from products.models import Product

User = get_user_model()


class OrderItemManager(models.Manager):
    def add_new_item(self, order, id, product_id, qty):
        item = OrderItem()
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound("Product not found")
        item.order_id = order
        item.product = product
        item.qty = qty
        item.price = product.price
        item.full_clean()
        item.save()

    def update_item(self, id, product_id, qty):
        item = OrderItem.objects.get(id=id)
        item.qty = qty
        item.full_clean()
        item.save()

    def delete_item(self, id):
        try:
            item = OrderItem.objects.get(id=id)
            item.delete()
        except OrderItem.DoesNotExist:
            raise NotFound("Item not found")


class OrderManager(models.Manager):
    def add_or_update(self, user, id, customer_id, description, order_date, shipping_date):
        order = Order()
        if id != 0:
            order = self.get_queryset().get(id=id)
        order.customer_id = customer_id
        order.created_user = user
        order.order_date = order_date
        order.shipping_date = shipping_date
        order.description = description
        order.full_clean()
        order.save()
        return order

    def get_last_week_orders(self):
        last_week = date.today()-timedelta(days=7)
        return self.get_queryset().filter(order_date__gte=last_week).values('order_date').annotate(total_orders=Count('order_date'))


class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField()
    shipping_date = models.DateField()
    description = models.TextField()

    objects = OrderManager()

    def clean(self):
        if self.order_date < date.today():
            raise ValidationError("Order date must be greater than today!")
        if self.shipping_date < date.today():
            raise ValidationError("Shipping date must be greater than today!")

    @property
    def total(self):
        return self.myorder.values('price', 'qty').aggregate(sum=Sum(F('price') * F('qty'), output_field=FloatField()))['sum']


class OrderItem(BaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="myorder")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=19)

    objects = OrderItemManager()

    def clean(self):
        if self.qty <= 0:
            raise ValidationError("Quantity cannot be 0 or negative!")
