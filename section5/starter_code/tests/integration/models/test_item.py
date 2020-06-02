from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)
            # verify item does not exist
            self.assertIsNone(ItemModel.find_by_name('test'))
            # add item to db
            item.save_to_db()
            # verify item exists in db
            self.assertIsNotNone(ItemModel.find_by_name('test'))

