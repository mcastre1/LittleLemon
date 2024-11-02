from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Salad", price=5.0, inventory = 1)
        MenuItem.objects.create(title="Soup", price=3.50, inventory = 1)
        MenuItem.objects.create(title="Burger", price=8.00, inventory = 1)
        
    def test_getall(self):
        response = self.client.get('menu/')
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        
        #self.assertEqual(response.data, serializer.data) 
        self.assertEqual(response.status_code, 200)