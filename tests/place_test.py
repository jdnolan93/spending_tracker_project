import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place("Woolworths")

    def test_if_place_has_name(self):
        self.assertEqual("Woolworths", self.place.place_name)