import re
'''
total=0
fh=open()
fvar=fh.read()
y=re.findall('[0-9]+',fvar)
for i in y:
    total=total+int(i)
print total
'''
import re
print sum( [for i in re.findall('[0-9]+',"regex_sum_167971.txt".read()) ] )
