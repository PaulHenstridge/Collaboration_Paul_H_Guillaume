import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Drunken Sailor", 0, ["Whiskey Sour", "Beer", "Wine", "Pina Collada"])

    def test_pub_has_drink__found(self):
        has_beer = self.pub.has_drink("Beer")
        self.assertTrue(has_beer)