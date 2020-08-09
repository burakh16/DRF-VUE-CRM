from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from customers.models import Customer
from .serializers import CustomerSerializer
from common.paginations import CustomPagination


class CustomerViewSet(ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomPagination

    @action(detail=False, methods=["GET"], url_path="get-without-pages")
    def get_without_pages(self, request):
        serializer = self.serializer_class(Customer.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)