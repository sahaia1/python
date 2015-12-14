#!/usr/bin/python

def func():
	try:
		if True:
			print "hello world"
	finally:
		print "finally"


func()