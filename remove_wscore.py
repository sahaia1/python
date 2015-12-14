import fileinput
import re

for line in fileinput.input(inplace=True):
	if re.search(r"ws-core.canon", line):
		print "import \"williamssonoma-comman.canon\";"
	else:
		print line,
