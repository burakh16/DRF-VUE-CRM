from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework import status

from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Customer
from .api.views import CustomerViewSet

factory = APIRequestFactory()


class CustomerTestAPI(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="ulan_mask", password="tesla"
        )
        self.customer_list_view = CustomerViewSet.as_view({"get": "list", })
        self.customer_without_pages_view = CustomerViewSet.as_view(
            {"get": "get_without_pages", })
        self.customer_create_view = CustomerViewSet.as_view(
            {"post": "create", })
        self.customer_detail_view = CustomerViewSet.as_view(
            {"get": "retrieve", })
        self.customer_delete_view = CustomerViewSet.as_view(
            {"delete": "destroy", })
        self.customer_update_view = CustomerViewSet.as_view(
            {"put": "update", })

    def _create_customer(self):
        url = reverse('customer-list')
        customer = {"name": "Customer 1", "address": "Customer 1",
                    "district": "nowhere", "city": "Barcelona",
                    "tax_office": "tax123", "tax_no": "123", "cell_number": "12345678"}
        request = factory.post(url, customer)
        force_authenticate(request, user=self.user)
        return self.customer_create_view(request)

    def _get_customer(self, id):
        url = reverse('customer-detail', kwargs={'pk': id})
        request = factory.get(url)
        force_authenticate(request, user=self.user)
        return self.customer_detail_view(request, pk=id)

    def _get_all_customers(self):
        url = reverse('customer-list')
        request = factory.get(url)
        force_authenticate(request, user=self.user)

        return self.customer_list_view(request)

    def _get_customers_without_pages(self):
        url = reverse('customer-get-without-pages')
        request = factory.get(url)
        force_authenticate(request, user=self.user)

        return self.customer_without_pages_view(request)

    def _update_customer(self, id):
        url = reverse('customer-detail', kwargs={'pk': id})
        customer = {"name": "Customer 1", "address": "lorem",
                    "district": "somewhere", "city": "Barcelona",
                    "tax_office": "tax123", "tax_no": "123", "cell_number": "12345678"}
        request = factory.put(url, customer)
        force_authenticate(request, user=self.user)

        return self.customer_update_view(request, pk=id)

    def _delete_customer(self, id):
        url = reverse('customer-detail', kwargs={'pk': id})
        request = factory.delete(url)
        force_authenticate(request, user=self.user)

        return self.customer_delete_view(request, pk=id)

    def test_create_customer(self):
        """
        Create a customer
        """
        response = self._create_customer()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'Customer 1')

    def test_detail_customer(self):
        """
        Get detail of a customer
        """
        customer_response = self._create_customer()
        customer_id = customer_response.data['id']

        response = self._get_customer(customer_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.get().id, customer_id)

    def test_list_customer(self):
        """
        List of customers
        """
        self._create_customer()
        self._create_customer()
        self._create_customer()

        response = self._get_all_customers()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["pagination"]["total"], 3)

    def test_customer_without_pages(self):
        """
        List of available customers
        """
        self._create_customer()
        self._create_customer()
        self._create_customer()

        response = self._get_customers_without_pages()
        print(len(list(response.data)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(list(response.data)), 3)

    def test_update_customer(self):
        """
        Update a customer
        """
        customer_response = self._create_customer()
        customer_id = customer_response.data['id']

        response = self._update_customer(customer_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_customer(self):
        """
        Delete a customer
        """
        customer_response = self._create_customer()
        customer_id = customer_response.data['id']

        response = self._delete_customer(customer_id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
