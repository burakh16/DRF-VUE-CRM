from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from products.models import Product
from .serializers import ProductSerializer
from common.paginations import CustomPagination


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    @action(detail=False, methods=["GET"])
    def available(self, request):
        serializer = self.serializer_class(Product.objects.available_products(), many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)