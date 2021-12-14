import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag = Tag("Food", True)

    def test_if_tag_has_name(self):
        self.assertEqual("Food", self.tag.tag_name)

    def test_if_tag_is_active(self):
        self.assertEqual(True, self.tag.active)