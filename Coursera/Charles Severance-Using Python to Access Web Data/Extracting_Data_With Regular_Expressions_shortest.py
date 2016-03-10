import re
print ( sum( [ int(e) for e in re.findall('[0-9]+', open('regex_sum_248476.txt').read() ) ] ) )