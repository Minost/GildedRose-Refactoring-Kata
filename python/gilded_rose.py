# -*- coding: utf-8 -*-


class GildedRose(object):
    """
    Represent the Gilded Rose Inn.
    Items sold by the innkeeper are of different types and each type of items has some special rules.
    Those rules are described in the update_quality function.
    """

    def __init__(self, items: list):
        """
        Initialize items list.
        :param items: list of item
        """
        self.items = items

    def update_quality(self):
        """
        Update the quality of items contained in the list
        """
        # For each item of items
        for item in self.items:
            # Condition on item name
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                # Condition on item quality
                if item.quality > 0:
                    # Condition on item name
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        # Decrease item quality
                        item.quality = item.quality - 1
            else:
                # Condition on item quality
                if item.quality < 50:
                    # Increase item quality
                    item.quality = item.quality + 1
                    # Condition on item name
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        # Condition on item remaining days
                        if item.sell_in < 11:
                            # Condition on item quality
                            if item.quality < 50:
                                # Increase item quality
                                item.quality = item.quality + 1
                        # Condition on item remaining days
                        if item.sell_in < 6:
                            # Condition on item quality
                            if item.quality < 50:
                                # Increase item quality
                                item.quality = item.quality + 1
            # Condition on item name
            if item.name != "Sulfuras, Hand of Ragnaros":
                # Decrease item remaining days
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                # Condition on item name
                if item.name != "Aged Brie":
                    # Condition on item name
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        # Condition on item quality
                        if item.quality > 0:
                            # Condition on item name
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                # Decrease item quality
                                item.quality = item.quality - 1
                    else:
                        # Update item quality
                        item.quality = 0
                else:
                    # Condition on item quality
                    if item.quality < 50:
                        # Increase item quality
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        """
        Initialize an item.
        :param name: the name of the item
        :param name: the number of days to sell the item
        :param name: the quality of the item
        """
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
