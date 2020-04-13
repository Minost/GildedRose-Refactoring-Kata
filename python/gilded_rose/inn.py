# -*- coding: utf-8 -*-
import json

from gilded_rose.gilded_rose import GildedRose, GildedRoseItem


def run(days: int, filename: str):
    print("OMGHAI!")

    with open(filename) as json_file:
        items = [GildedRoseItem.from_json(item) for item in json.load(json_file)["items"]]

        for day in range(days):
            print("-------- day %s --------" % day)
            print("name, sellIn, quality")
            for item in items:
                print(item)
            print("")
            GildedRose(items).update_quality()
