# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_standard_items(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Elixir of the Mongoose", sell_in=0, quality=20),
            Item(name="Elixir of the Mongoose", sell_in=-1, quality=20),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(18, items[1].quality)
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(18, items[2].quality)
        self.assertEqual(-2, items[2].sell_in)

    def test_aging_items(self):
        items = [
            Item(name="Aged Brie", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=0, quality=50),
            Item(name="Aged Brie", sell_in=-1, quality=50),
            Item(name="Aged Brie", sell_in=0, quality=20),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(50, items[1].quality)
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(50, items[2].quality)
        self.assertEqual(-2, items[2].sell_in)
        self.assertEqual(22, items[3].quality)
        self.assertEqual(-1, items[3].sell_in)

    def test_epic_items(self):
        items = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(80, items[1].quality)
        self.assertEqual(0, items[1].sell_in)
        self.assertEqual(80, items[2].quality)
        self.assertEqual(-1, items[2].sell_in)

    def test_ticket_items(self):
        items = [
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(22, items[1].quality)
        self.assertEqual(9, items[1].sell_in)
        self.assertEqual(23, items[2].quality)
        self.assertEqual(4, items[2].sell_in)
        self.assertEqual(0, items[3].quality)
        self.assertEqual(-1, items[3].sell_in)

    def test_conjured_items(self):
        items = [
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),
            Item(name="Conjured Mana Cake", sell_in=0, quality=6),
            Item(name="Conjured Mana Cake", sell_in=-1, quality=6),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[1].quality)
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(4, items[2].quality)
        self.assertEqual(-2, items[2].sell_in)


if __name__ == '__main__':
    unittest.main()
