import urllib.parse
import urllib.request
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    print ('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data),'characters')
    js = json.loads(data.decode('utf-8'))
    # print (json.dumps(js, indent=4))
    place_id = js["results"][0]['place_id']
    print (place_id)

# South Federal University
# Universidad Central de Venezuela