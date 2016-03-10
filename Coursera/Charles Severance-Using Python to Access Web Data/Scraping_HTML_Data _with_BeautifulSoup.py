import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
total = 0
for tag in tags:
    total += int(tag.contents[0])
    # print ('TAG:',tag)
    # print ('URL:',tag.get('href', None))
    # print ('Contents:',tag.contents[0])
    # print ('Attrs:',tag.attrs)
print ('sum:', total)
