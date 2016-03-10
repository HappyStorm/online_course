import urllib.request

urlhand = urllib.request.urlopen('http://www.pythonlearn.com/code/intro-short.txt')
print (urlhand.info())
print (type (urlhand.info()))