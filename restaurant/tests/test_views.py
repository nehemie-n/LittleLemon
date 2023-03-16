from django.test import TestCase
from ..models import Booking, Menu


class MenuView(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Food", price=21, inventory=12)
        item = Menu.objects.get(id=item.id)
        self.assertIsNotNone(item.title)
        self.assertEqual(item.title, "Food")
