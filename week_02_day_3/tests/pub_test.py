import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food


class TestPub(unittest.TestCase):
    def setUp(self):
        self.whiskey_sour = Drink("Whiskey Sour", 8.0, 1)
        self.beer = Drink("Beer", 4.0, 2)
        self.wine = Drink("Wine", 6.0, 3)
        self.drinks_list = [self.whiskey_sour, self.beer, self.wine]
        self.customer = Customer("John Lennon", 50, 50, 5)
        self.customer_underage = Customer("Junior Lennon", 5, 15, 0)
        self.customer_wasted = Customer("Boozy Lennon", 5, 15, 20)
        self.food1 = Food("fried crickets", 1, 1)
        self.food2 = Food("fermented tofu", 3, 2)
        self.food3 = Food("kangaroo steak", 5, 3)
        self.menu = [self.food1.name, self.food2.name, self.food3.name]
        self.inventory = {key: 20 for key in self.menu}
        self.pub = Pub("The Drunken Sailor", 0, self.drinks_list, self.inventory)

    # def test_pub_has_drink__found(self):
    #     has_beer = self.pub.has_drink(self.beer)
    #     self.assertTrue(has_beer)

    def test_add_to_till(self):
        self.pub.add_to_till(10)
        self.assertEqual(10, self.pub.till)

    def test_find_drink_by_name(self):
        drink = self.pub.find_drink_by_name("Beer")
        self.assertEqual("Beer", drink.name)

    def test_customer_is_not_wasted__fail(self):
        self.assertFalse(self.pub.customer_is_not_wasted(self.customer_wasted))

    def test_sell_a_drink__sucess(self):
        drink = self.pub.find_drink_by_name("Beer")
        price = drink.price
        self.customer.reduce_wallet(price)
        self.pub.add_to_till(price)
        self.assertTrue(self.customer.can_pay(price))
        self.assertTrue(self.pub.customer_is_not_wasted(self.customer))
        self.assertEqual(4, self.pub.till)
        self.assertEqual(46, self.customer.wallet)

    def test_can_buy_food(self):
        pass

    def test_can_rejuvinate(self):
        self.customer.rejuvinate(self.menu[2])
        self.assertEqual(2, self.customer.drunkenness)

    def test_update_inventory(self):
        self.pub.sell_food(self.customer, self.food1)
        self.assertEqual(19, self.pub.update_inventory(self.food1))
