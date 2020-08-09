from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework import status

from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Product
from .api.views import ProductViewSet

factory = APIRequestFactory()


class ProductTestAPI(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="ulan_mask", password="tesla"
        )
        self.product_list_view = ProductViewSet.as_view({"get": "list", })
        self.product_available_view = ProductViewSet.as_view({"get": "available", })
        self.product_create_view = ProductViewSet.as_view({"post": "create", })
        self.product_detail_view = ProductViewSet.as_view(
            {"get": "retrieve", })
        self.product_delete_view = ProductViewSet.as_view(
            {"delete": "destroy", })
        self.product_update_view = ProductViewSet.as_view(
            {"put": "update", })

    def _create_product(self, qty=1000):
        url = reverse('product-list')
        product = {"code": "product-1", "name": "Product 1",
                   "price": 16.5, "qty": qty, "description": "lovely product"}
        request = factory.post(url, product)
        force_authenticate(request, user=self.user)
        return self.product_create_view(request)

    def _get_product(self, id):
        url = reverse('product-detail', kwargs={'pk': id})
        request = factory.get(url)
        force_authenticate(request, user=self.user)
        return self.product_detail_view(request, pk=id)

    def _get_all_products(self):
        url = reverse('product-list')
        request = factory.get(url)
        force_authenticate(request, user=self.user)

        return self.product_list_view(request)
    
    def _get_available_products(self):
        url = reverse('product-available')
        request = factory.get(url)
        force_authenticate(request, user=self.user)

        return self.product_available_view(request)

    def _update_product(self, id):
        url = reverse('product-detail', kwargs={'pk': id})
        product = {"code": "some-new-code","name": "some new product name", "price":20.22, "qty": 2000}
        request = factory.put(url, product)
        force_authenticate(request, user=self.user)

        return self.product_update_view(request, pk=id)

    def _delete_product(self, id):
        url = reverse('product-detail', kwargs={'pk': id})
        request = factory.delete(url)
        force_authenticate(request, user=self.user)

        return self.product_delete_view(request, pk=id)

    def test_create_product(self):
        """
        Create a product
        """
        response = self._create_product()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Product 1')

    def test_detail_product(self):
        """
        Get detail of a product
        """
        product_response = self._create_product()
        product_id = product_response.data['id']

        response = self._get_product(product_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get().id, product_id)

    def test_list_product(self):
        """
        List of products
        """
        self._create_product(1000)
        self._create_product(2000)
        self._create_product(3000)

        response = self._get_all_products()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["pagination"]["total"], 3)
    
    def test_available_product(self):
        """
        List of available products
        """
        self._create_product(0)
        self._create_product(2000)
        self._create_product(3000)

        response = self._get_available_products()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["pagination"]["total"], 2)

    def test_update_product(self):
        """ 
        Update a product
        """
        product_response = self._create_product()
        product_id = product_response.data['id']

        response = self._update_product(product_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_product(self):
        """ 
        Delete a product
        """
        product_response = self._create_product()
        product_id = product_response.data['id']

        response = self._delete_product(product_id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
