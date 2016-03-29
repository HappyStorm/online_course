#!/usr/bin/python

import sys

numSales = 0
totalSales = 0
oldKey = None

# Loop around the data
# It will be in the format val
# Where val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip()
    if len(data_mapped) != 1:
        continue

    thisSale = data_mapped
    thisSale = float(thisSale)

    totalSales += thisSale
    numSales += 1

print 'Num of Sales: ', numSales, 'Total Value: ', totalSales
