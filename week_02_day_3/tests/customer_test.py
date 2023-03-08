import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John Lennon", 50)

    def test_customer_has_name(self):
        self.assertEqual("John Lennon", self.customer.name)