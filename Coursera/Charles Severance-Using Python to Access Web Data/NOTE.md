The webpage use several languages and formats to communicate with the appliecations(client) and servers(host)

The following notes are my learning experience of taking this course:

Week 2:
	Part 1: Regular Expression Quick Guide
		^	Matches the beginning of a line
		$	Matches the end of the line
		.	Matches any character
		\s	Matches whitespace
		\S	Matches any non-whitespace character
		*	Repeats a character zero or more times
		*?	Repeats a character zero or more times (non-greedy)
		+	Repeats a character one or more times
		+?	Repeats a character one or more times (non-greedy)
		[aeiou]	Matches a single character in the listed set
		[^XYZ]	Matches a single character not in the listed set
		[a-z0-9]	The set of characters can include a range
		(	Indicates where string extraction is to start
		)	Indicates where string extraction is to end

Week 3:
	Part 1: Difference between using "urllib" by Python 2.x and Python 3.x
		Python 2.x use "urllib" to operate on the URls directly.
			For example:
				urlhand = urllib.urlopen('http://www.pythonlearn.com/code/intro-short.txt')
			then you could get sth like the file handler

		Python 3.x use "urllib.x" to operate on different usage of the URLs.
			For example:
				if you want to open the url, then you should type
					import urllib.request

					urlhand = urllib.request.urlopen('http://www.pythonlearn.com/code/intro-short.txt')"
				else if you want to encode the url, then you need to type
					import urllib.parse

				    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
		And these are the small part of the differences between Python 2.x and Python 3.x
	
	Part 2: Brief introduction to using "urllib"

Week 4:
	Part 1: HTML Retrieving
		HTTP protocol includes several tags,
		e.g., <h1>...</h1,>, <a href="..." </a>, <p>...</p>

				  GET
		       -------->
		Client 			 Server
		       <--------
		          HTML

    Part 2: BeautifulSoup
    	There exists a powerful and beautiful library which can help you parsing the HTML format, it called "BeautifulSoup"
    		For example:
    			...
				from bs4 import BeautifulSoup

				url = input('Enter - ')
				html = urllib.request.urlopen(url).read()
				soup = BeautifulSoup(html)

				# Retrieve all of the anchor tags
				tags = soup('span')
				...
				for tag in tags:
				    ...
				    # print ('TAG:', tag)
				    # print ('URL:', tag.get('href', None))
				    # print ('Contents:', tag.contents[0])
				    # print ('Attrs:', tag.attrs)
				...

			Another example:
				...
				from bs4 import *
				...

				...
					html = urllib.request.urlopen(url).read()
					soup = BeautifulSoup(html, 'lxml')
					tags = soup('a')
					url = tags[2].get('href', None)
				...
				
Week 5:
	Part 1: XML
		XML is a universal format which packages(serialize) the infomation and transmits it to another side to be extracted(de-serialize)
		In other words,

											 XML, JSON
											----------->
		Client(application)	--> Serialize		Info 		De-Serialize <-- Server(webpage)
											<-----------
											 XML, JSON

		And its format will be looked like:
			<people>						<------ "Start Tag"
				<person>
					<name>Haley</name>
					<phone type="intl">		<------ "Attribute" => type="intl"
						+886 123			<------ "Content"
					</phone>
					<email hide="yes" />	<------ "Self Closing Tag"
				</persion>
			</people>						<------ "End Tag"

	Part 2: XML Tree Structure
		The above structure is so called "Tree Structure". Thus, Python has its build-in library for XML-Parsing.
			For example:
				...
				import xml.etree.ElementTree as ET
				...
				...
					uh = urllib.request.urlopen(url_actual)
				data = uh.read()
				tree = ET.fromstring(data)
				counts = tree.findall('.//count')
				...
			Then the counts will be a type list.

Week 6:
	Part 1: JavaScript Object Notation
		JSON is the abbreviation of the "JavaScript Object Notation". It's also one of the formats used to transform the data. Unlike the XML-Format, JSON is simple and easy to transform between Python and Java.
		It has types "array" (list in Python), "dictionary" (hashmap in JAVA).
		And it's also the built-in library in Python.
		For example:
			...
			import json
			...
				uh = urllib.request.urlopen(url_actual)
			data = uh.read()

			# since the data retrieved from the above url contains char 'b' in the prefix,
			# the json treat it as a byte string, so it need to be decode by 'UTF-8'
			info = json.loads(data.decode('utf-8'))
			...
			for item in info['comments']:
			    total += item['count']
			...
		Another example:
			...
			import json
			...
			    uh = urllib.request.urlopen(url)
			    data = uh.read()
			    ...
			    js = json.loads(data.decode('utf-8'))
			    # print (json.dumps(js, indent=4))
			    place_id = js["results"][0]['place_id']
			    ...
