import fileinput
import re
import sys

for line in fileinput.input(sys.argv[1]):
  if re.search(sys.argv[2], line):
    print line,
