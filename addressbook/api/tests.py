from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from contacts.models import Contact

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.contact = Contact.objects.create(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            phone_number="1234567890",
            address="123 Test St"
        )
    
    def test_contact_list(self):
        url = reverse('contact-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)