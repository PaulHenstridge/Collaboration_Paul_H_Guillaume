import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John Lennon", 50, 50, 5)

    def test_customer_has_name(self):
        self.assertEqual("John Lennon", self.customer.name)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(10)
        self.assertEqual(40, self.customer.wallet)

    def test_can_pay_for_drink__true(self):
        enough_money = self.customer.can_pay_for_drink(10)
        self.assertTrue(enough_money)

    def test_can_pay_for_drink__false(self):
        enough_money = self.customer.can_pay_for_drink(100)
        self.assertFalse(enough_money)
