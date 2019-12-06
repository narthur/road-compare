#!/usr/bin/env python3

from road_compare.main import Main
from natlibpy.factory import Factory
import sys

if len(sys.argv) < 3:
    print('Usage:')
    print('./main.py https://www.beeminder.com/user/before.json https://www.beeminder.com/user/after.json')
    print('./main.py before.json after.json')
    exit()

before_address = sys.argv[1]
after_address = sys.argv[2]

factory = Factory()
main = factory.make(Main)

main.run(before_address, after_address)
