#!/usr/bin/python

import sys

address_MAX = None
MAX = 0
old_Address = None
count = 0
# Loop around the data
# It will be in the format val
# Where val is the address

for line in sys.stdin:
    new_Address = line.strip()

    if old_Address and old_Address != new_Address:
		if count >= MAX:
		    MAX = count
		    address_MAX = old_Address
			count = 0

    old_Address = new_Address
    count += 1

print 'PathName: {0}, NumOccurrence: {1}'.format(address_MAX, MAX)
