# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
filevar = fh.read()
filevar = filevar.upper()
print filevar