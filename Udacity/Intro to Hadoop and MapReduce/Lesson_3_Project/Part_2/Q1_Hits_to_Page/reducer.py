#!/usr/bin/python

import sys

count = 0
# Loop around the data
# It will be in the format val
# Where val is the specific address

for line in sys.stdin:
    new_Address = line.strip()

    if new_Address == '/assets/js/the-associates.js'
    	count += 1

print 'Hits: ', count
