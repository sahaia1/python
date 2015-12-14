import fileinput

for line in fileinput.input("abc.txt", inplace=True):
	if fileinput.lineno() == 1:
		print 'Aditya'
	else:
		print line
