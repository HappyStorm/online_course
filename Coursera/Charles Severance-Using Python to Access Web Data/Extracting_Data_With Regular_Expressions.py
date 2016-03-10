import re

hand = open('regex_sum_248476.txt')
total = 0
num_value = 0
numlist = list()
for line in hand:
	line = line.strip()
	stuff = re.findall('([0-9]+)', line)
	for e in stuff:	
		total += int(e)
	num_value += len(stuff)
print ('There are {0} values with a sum {1}'.format(num_value, total))
