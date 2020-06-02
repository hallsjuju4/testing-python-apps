from unittest import TestCase
from models.item import ItemModel

class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 19.99)
        self.assertEqual(item.name, 'test', "the name of the item does not match expected result")
        self.assertEqual(item.price, 19.99, "the price of the item does not match expected result")

    def test_item_json(self):
        item = ItemModel('test', 19.99)
        expected = {'name': 'test', 'price': 19.99}
        self.assertEqual(item.json(), expected, "the item JSON does not match expected result")
