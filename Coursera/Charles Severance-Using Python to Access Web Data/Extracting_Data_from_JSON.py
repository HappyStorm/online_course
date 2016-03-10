import urllib.request
import json

# url_sample equals to the sample test url
url_sample = 'http://python-data.dr-chuck.net/comments_42.json'
# url_actual equals to the actual test url
url_actual = 'http://python-data.dr-chuck.net/comments_248482.json'

exe = input('Please enter the executing type(0 for sample, 1 for actual): ')
if exe == '0':
	uh = urllib.request.urlopen(url_sample)
else:
	uh = urllib.request.urlopen(url_actual)
data = uh.read()

# since the data retrieved from the above url contains char 'b' in the prefix,
# the json treat it as a byte string, so it need to be decode by 'UTF-8'
info = json.loads(data.decode('utf-8'))

total = 0
for item in info['comments']:
    total += item['count']
print (total)
