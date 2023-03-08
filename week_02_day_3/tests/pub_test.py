import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    def setUp(self):
        self.whiskey_sour = Drink("Whiskey Sour", 8.0)
        self.beer = Drink("Beer", 4.0)
        self.wine = Drink("Wine", 6.0)
        drinks_list = [self.whiskey_sour, self.beer, self.wine]
        self.pub = Pub("The Drunken Sailor", 0, drinks_list)
        self.customer = Customer("John Lennon", 50)

    def test_pub_has_drink__found(self):
        has_beer = self.pub.has_drink(self.beer)
        self.assertTrue(has_beer)

    def test_add_to_till(self):
        self.pub.add_to_till(10)
        self.assertEqual(10, self.pub.till)

    def test_sell_a_drink(self):


