import unittest
from models.purchase import Purchase

class TestPurchase(unittest.TestCase):

    def setUp(self):
        self.purchase = Purchase(3.33, "Tesco", "Beans")

    def test_if_has_price(self):
        self.assertEqual(3.33, self.purchase.price)

    def test_if_has_place(self):
        self.assertEqual("Tesco", self.purchase.place)