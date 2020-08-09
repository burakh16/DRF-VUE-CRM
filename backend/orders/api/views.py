import datetime

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from orders.models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer, OrdersDisplaySerializer
from common.paginations import CustomPagination


class OrderViewSet(ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return OrdersDisplaySerializer
        return super().get_serializer_class()

    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = Order.objects.add_or_update(
            request.user, **serializer.validated_data)
        for item in request.data["items"]:
            order_item = OrderItemSerializer(data=item)
            order_item.is_valid(raise_exception=True)
            OrderItem.objects.add_new_item(
                order.id, **order_item.validated_data)
        return Response(status=status.HTTP_201_CREATED)
     
    def update(self, request, pk=None):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = Order.objects.add_or_update(
            request.user, **serializer.validated_data)
        for item in request.data["items"]:
            order_item = OrderItemSerializer(data=item)
            order_item.is_valid(raise_exception=True)
            if order_item.validated_data["id"] != 0:
                OrderItem.objects.update_item(**order_item.validated_data)
            else:
                OrderItem.objects.add_new_item(
                order=pk, **order_item.validated_data)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["delete"], url_path="item-delete")
    def item_delete(self, request, pk):
        OrderItem.objects.delete_item(pk)
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="report")
    def get_last_week_report(self, request, *args, **kwargs):
        serializer = Order.objects.get_last_week_orders()
        return Response(serializer,status=status.HTTP_200_OK)