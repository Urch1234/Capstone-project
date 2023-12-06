from decimal import Decimal
from django.test import TestCase
from restaurant.models import Menu


class MenuModelTest(TestCase):
    def setUp(self):
        # Create test data:
        self.menu1 = Menu.objects.create(
            name="Pizza Margherita",
            price=15.99,
            menu_item_description="classic pizza with tomato sauce, mozzarella cheese, and basil.",
        )
        self.menu2 = Menu.objects.create(
            name="Jollof Rice",
            price=29.65,
            menu_item_description="Well seasoned oriental dish with a touch sprinkled vegetables",
        )

    def test_menu_name(self):
        self.assertEqual(self.menu1.name, "Pizza Margherita")
        self.assertEqual(self.menu2.name, "Jollof Rice")

    def test_menu_price(self):
        self.assertEqual(self.menu1.price, Decimal("15.99"))
        self.assertEqual(self.menu2.price, Decimal("29.65"))

    def test_menu_item_description(self):
        self.assertEqual(
            self.menu1.menu_item_description,
            "classic pizza with tomato sauce, mozzarella cheese, and basil.",
        )
        self.assertEqual(
            self.menu2.menu_item_description,
            "Well seasoned oriental standard dish with a touch sprinkled vegetables",
        )

    def test_string_registration(self):
        self.assertEqual(str(self.menu1), "Pizza Margherita : 15.99")
        self.assertEqual(str(self.menu2), "Jollof Rice : 29.65")
