import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/comments_167976.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('span')
values = []
for tag in tags:
    values.append(int(tag.contents[0]))
print sum(values)

