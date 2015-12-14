from subprocess import call

import re
import os
import fileinput
import sys

def removeLines(file):
    path = "/tmp/" + file
    for line in fileinput.input(path, inplace=True):
	if re.search(r"Process file", line) or re.search(r"Success!", line):
		continue
	else:
		print line,

def sucregen(domainFile, move):
    backend = "/Users/adityasahai/br/work/src/backend/"
    sucpath = backend + "/configs/site-url-patterns/site-url-classifier.js"
    canontestdir = backend + "/configs/site-url-patterns/tests/canonical"
    canontest= backend + "/dist/br-run.sh SiteUrlPatterns canon_test --pat " + sucpath
    cmd = canontest + " -d " + domainFile + " --regen " + " --input=" + domainFile + " > /tmp/" + domainFile
    call(cmd, shell=True)
    removeLines(domainFile)
    if move == True:
        cmd2 = "mv /tmp/" + domainFile + " " + canontestdir + "/"
        call(cmd2, shell=True)

def extractAndPlaceURLs(file, dir):
    try:
        fd = open(file, "r")
    except IOError:
        print "Invalid File Name: Please check again!"
        exit()

    testfilename = dir + "/" + file
    fd2 = open(testfilename, "w")
    for lines in fd.readlines():
        if not re.search(r"^\|", lines):
            fd2.write(lines)
    fd2.close()
    fd.close()

def createTestFiles(dir, domain):
    path = "/Users/adityasahai/br/work/src/backend/configs/site-url-patterns/tests/canonical"
    os.chdir(path)
    extractAndPlaceURLs(domain, dir)

def runTest(dir, domain, move = False):
    os.chdir(dir)
    sucregen(domain, move)
    print "file - " + domain + " Done"

def main():
    move = False
    new_dir = r"/Users/adityasahai/test_dir"
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    createTestFiles(new_dir, sys.argv[1])
    if sys.argv[2] == "true":
        move = True
    runTest(new_dir, sys.argv[1], move)

if __name__ == "__main__":
    main()
