import urllib.request
from bs4 import *

# url_sample equals to the sample test url
url_sample = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
# url_actual equals to the actual test url
url_actual = 'http://python-data.dr-chuck.net/known_by_Believe.html'

exe = input('Please enter the executing type(0 for sample, 1 for actual): ')
if exe == '0':
	for i in range(4):
		print (url)
		html = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(html, 'lxml')
		tags = soup('a')
		url = tags[2].get('href', None)
else:
	for i in range(7):
		print (url)
		html = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(html, 'lxml')
		tags = soup('a')
		url = tags[17].get('href', None)
print (url)
