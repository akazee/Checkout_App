from django.test import TestCase
from checkout.models import *

# Tests for models
class TestModels(TestCase):

    # Setup for our test cases
    def setUp(self):
        self.recipt1 = recipt.objects.create(text="test recipt")
        self.item1 = item.objects.create(name="test item", price=10.00)
        self.id = self.item1.id
        self.recipt1.items.add(self.item1)

    # Test to ensure each recipt model is assigned a text attribute upon creation
    def test_recipt_is_assigned_text(self):
        self.assertEquals(self.recipt1.text, "test recipt")
    
    # Testing the hasItem method from recipt
    def test_recipt_hasItem(self):
        self.assertTrue(self.recipt1.hasItem(self.id))
        self.assertFalse(self.recipt1.hasItem(-1))

    
    