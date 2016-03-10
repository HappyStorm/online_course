import urllib.request
import xml.etree.ElementTree as ET

# url_sample equals to the sample test url
url_sample = 'http://python-data.dr-chuck.net/comments_42.xml'
# url_actual equals to the actual test url
url_actual =  'http://python-data.dr-chuck.net/comments_248478.xml'

exe = input('Please enter the executing type(0 for sample, 1 for actual): ')
if exe == '0':
	uh = urllib.request.urlopen(url_sample)
else:
	uh = urllib.request.urlopen(url_actual)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
total = 0
for i in range(len(counts)):
    total += int(counts[i].text)
print (total)
