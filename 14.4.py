'''
In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py.
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment.
One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2482)
Actual data: http://python-data.dr-chuck.net/comments_167977.json (Sum ends with 2)

'''
import json
import urllib


url = 'http://python-data.dr-chuck.net/comments_167977.json'


uh = urllib.urlopen(url)
data = uh.read()
info = json.loads(data)
jsoncomments = info["comments"]
sum=0
for test in jsoncomments:
    sum=sum+int(test["count"])

print sum

