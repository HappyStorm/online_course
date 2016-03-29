#!/usr/bin/python

import sys

salesMax = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store (store name), val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesMax
        oldKey = thisKey
        salesMax = 0

    if thisSale >= salesMax:
	   salesMax = thisSale

    oldKey = thisKey

if oldKey != None:
    print oldKey, "\t", salesMax
