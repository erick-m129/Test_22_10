from django.test import TestCase
from shop.models import Item
from django.urls import reverse

# Create your tests here.
class ItemTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            title = 'Test Item',
            description = 'Test Description',
            stock = 3
        )
    
    def test_items_list(self):
        response = self.client.get(reverse('shop:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item')