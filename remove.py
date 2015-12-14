import fileinput
import re

for line in fileinput.input(inplace=True):
	if re.search(r"Process file", line) or re.search(r"Success!", line):
		continue
	else:
		print line,
