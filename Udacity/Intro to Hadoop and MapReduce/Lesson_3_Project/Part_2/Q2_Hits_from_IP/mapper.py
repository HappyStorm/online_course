#!/usr/bin/python

# We want elements [0] (IP)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
       	ip, identity, username, time, zone, request, address, protocol, status, objsize = data
	time = time.replace('[', '')
	zone = zone.replace(']', '')
	request = request.replace('"', '')
	protocol = protocol.replace('"', '')	
	print "{0}".format(ip)
