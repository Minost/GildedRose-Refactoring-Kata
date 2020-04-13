# -*- coding: utf-8 -*-
import json
import unittest

from gilded_rose.gilded_rose import GildedRose, GildedRoseItem, GildedRoseStandardItem


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [GildedRoseStandardItem("foo", 0, 0)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("foo", items[0].name)

    def test_legendary_items(self):
        self.assert_equal_items("legendary")

    def test_standard_items(self):
        self.assert_equal_items("standard")

    def test_conjured_items(self):
        self.assert_equal_items("conjured")

    def test_aging_items(self):
        self.assert_equal_items("aging")

    def test_ticket_items(self):
        self.assert_equal_items("ticket")

    def assert_equal_items(self, item_type: str):
        with open('test/resources/test_items.json') as json_file:
            data = json.load(json_file)
            items = [GildedRoseItem.from_json(item) for item in data[item_type]["input"]]
            expected = [item for item in data[item_type]["output"]]

            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()

            items = [item.to_json() for item in items]
            self.assertEqual(items, expected)


if __name__ == '__main__':
    unittest.main()
