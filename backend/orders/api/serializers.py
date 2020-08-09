from rest_framework import serializers

from orders.models import Order, OrderItem


class OrdersDisplaySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    customer_name = serializers.ReadOnlyField(source="customer.name")
    description = serializers.CharField()
    order_date =serializers.CharField()
    order_date =serializers.CharField()
    shipping_date =serializers.CharField()
    total = serializers.ReadOnlyField()

   

class OrderItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    qty = serializers.IntegerField()
    product_code = serializers.ReadOnlyField(source="product.code")
    product_name = serializers.ReadOnlyField(source="product.name")
    product_description = serializers.ReadOnlyField(source="product.description")
    price = serializers.ReadOnlyField()


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField()
    customer_name = serializers.ReadOnlyField(source="customer.name")
    customer_id = serializers.IntegerField()
    order_date = serializers.DateField()
    shipping_date = serializers.DateField()
    total = serializers.ReadOnlyField()
    items = serializers.SerializerMethodField()

    def get_items(self, obj):
        return OrderItemSerializer(obj.myorder.all(), many=True).data
