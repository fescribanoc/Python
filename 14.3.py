import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_167973.xml'


xml = urllib.urlopen(url).read()
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
count = tree.findall('.//count')
suma=0
for num in count:
    suma= suma + int(num.text)
print suma

