from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import *

# Tests to make sure all our paths are working correctly
class TestUrls(SimpleTestCase):

    # Test to ensure the url path for create page is resolved
    def test_create_url_is_resolved(self):
        url = reverse('create')
        self.assertEquals(resolve(url).func, create)

    # Test to ensure the url path for the create page is resolved
    def test_index_url_is_resolved(self):
        url = reverse('index', args=[1])
        self.assertEquals(resolve(url).func, index)