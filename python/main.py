import sys

from gilded_rose.inn import run

if __name__ == "__main__":
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
        run(days, 'gilded_rose/resources/inventory.json')
