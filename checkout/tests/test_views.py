from django.test import TestCase, Client
from django.urls import reverse
from checkout.models import *
import json

# Tests to ensure our views are working correctly on client side
class TestViews(TestCase):

    # Setup for our view tests
    def setUp(self):
        self.cient = Client()
        self.create_url = reverse('create')

        recipt.objects.create(text="test recipt")
        self.index_url = reverse('index', args=[1])

    # Test to see if create.html is accessed from view.create
    def test_create_GET(self):
        response = self.client.get(self.create_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/create.html')
    
    # Tests to see if display.html is accessed from view.index
    def test_index_GET(self):
        response = self.client.get(self.index_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/display.html')

