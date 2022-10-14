from django.test import SimpleTestCase
from checkout.forms import *

class TestForms(SimpleTestCase):

    # Test that given the correct values, our new order form is valid
    def test_form_CreateNewOrder(self):
        form = CreateNewOrder(data={
            'name': 'test order'
        })

        self.assertTrue(form.is_valid())
    
    # Test that given the correct values, our new item form is valid
    def test_form_AddItem(self):
        form = AddItem(data={
            'name': 'test item',
            'price': 10.00
        })

        self.assertTrue(form.is_valid())