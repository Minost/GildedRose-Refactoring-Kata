# -*- coding: utf-8 -*-
from abc import abstractmethod
from enum import Enum
from typing import List

from lib.goblin import Item

MIN_QUALITY = 0
MAX_QUALITY = 50


class ItemType(Enum):
    LEGENDARY = 'LEGENDARY',
    STANDARD = 'STANDARD',
    CONJURED = 'CONJURED',
    AGING = 'AGING',
    TICKET = 'TICKET'


class GildedRoseItem(Item):
    """
    Represent an Item that can be sold at the inn.
    """

    @abstractmethod
    def update_quality(self):
        """
        This method will be used to define the update Quality process of each item types.
        """

    def decrease_quality(self, quantity: int):
        self.quality = max(MIN_QUALITY, self.quality - quantity)

    def increase_quality(self, quantity: int):
        self.quality = min(MAX_QUALITY, self.quality + quantity)

    def to_json(self):
        return {
            "name": self.name,
            "sell_in": self.sell_in,
            "quality": self.quality
        }

    @staticmethod
    def from_json(item: dict):
        name = item['name']
        sell_in = item['sell_in']
        quality = item['quality']
        family = item['family']

        switcher = {
            ItemType.LEGENDARY: GildedRoseLegendaryItem(name, sell_in, quality),
            ItemType.STANDARD: GildedRoseStandardItem(name, sell_in, quality),
            ItemType.CONJURED: GildedRoseConjuredItem(name, sell_in, quality),
            ItemType.AGING: GildedRoseAgingItem(name, sell_in, quality),
            ItemType.TICKET: GildedRoseTicketItem(name, sell_in, quality)
        }

        return switcher.get(ItemType[family])


class GildedRoseLegendaryItem(GildedRoseItem):
    def update_quality(self):
        """
        legendary items never has to be sold or decreases in Quality.
        """


class GildedRoseStandardItem(GildedRoseItem):
    def update_quality(self):
        """
        Standard items Quality decreases by 1.
        Once the sell by date has passed, Quality degrades twice as fast.
        """
        self.sell_in -= 1
        if self.sell_in >= 0:
            self.decrease_quality(1)
        else:
            self.decrease_quality(2)


class GildedRoseConjuredItem(GildedRoseItem):
    def update_quality(self):
        """
        Conjured items degrade in Quality twice as fast as Standard items.
        """
        self.sell_in -= 1
        if self.sell_in >= 0:
            self.decrease_quality(2)
        else:
            self.decrease_quality(4)


class GildedRoseAgingItem(GildedRoseItem):
    def update_quality(self):
        """
        Aging items increases in Quality the older it gets.
        Once the sell by date has passed, Quality increases twice as fast.
        """
        self.sell_in -= 1
        if self.sell_in >= 0:
            self.increase_quality(1)
        else:
            self.increase_quality(2)


class GildedRoseTicketItem(GildedRoseItem):
    def update_quality(self):
        """
        Ticket items increases in Quality as its SellIn value approaches.
        Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but.
        Quality drops to 0 after the concert.
        """
        self.sell_in -= 1
        if self.sell_in >= 0:
            if self.sell_in < 5:
                self.increase_quality(3)
            elif self.sell_in < 10:
                self.increase_quality(2)
            else:
                self.increase_quality(1)
        else:
            self.quality = 0


class GildedRose(object):
    """
    Represent the Gilded Rose Inn.
    Items sold by the innkeeper are of different types and each type of items has some special rules.
    Those rules are described in the update_quality function.
    """

    def __init__(self, items: List[GildedRoseItem]):
        """
        Initialize items list.
        :param items: list of item
        """
        self.items = items

    def update_quality(self):
        """
        Update the quality of items contained in the list
        """
        for item in self.items:
            item.update_quality()
