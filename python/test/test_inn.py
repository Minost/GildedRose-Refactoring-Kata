# -*- coding: utf-8 -*-
import sys

from gilded_rose.inn import run


def main():
    days = 2
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    run(days, 'test/resources/test_inventory.json')


if __name__ == "__main__":
    main()
