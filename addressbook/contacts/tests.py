from django.test import TestCase
from django.contrib.postgres.search import SearchVector
from .models import Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone_number="1234567890",
            address="123 Main St"
        )
    
    def test_contact_creation(self):
        self.assertEqual(self.contact.first_name, "John")
        self.assertEqual(self.contact.last_name, "Doe")
    
    def test_search_vector_update(self):
        self.contact.save()  # Triggers search vector update
        updated = Contact.objects.get(pk=self.contact.pk)
        self.assertIsNotNone(updated.search_vector)