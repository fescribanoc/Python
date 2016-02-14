'''
In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Keanna.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: Y
'''

import urllib
from BeautifulSoup import *


repeat=7
url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Keanna.html"
while repeat>0:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url= tags[17].get('href',None)
    print re.findall('[A-Z]\S+(?=.html)',url)
    repeat=repeat-1
'''
for tag in tags:
    repeat = repeat + 1

    print tag.get('href', None)
'''