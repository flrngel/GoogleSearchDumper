#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import os
import time
import subprocess

# THIS CODE IS FOR PERSONAL PERFORMANCE
# DO NOT USE WITHOUT UNDERSTANDING THIS CODE

def https_cnt():
	p=subprocess.Popen("../url_https_parser/url_parser.py ../test.txt | wc -l", stdout=subprocess.PIPE, shell=True)
	(output,err)=p.communicate()
	p_status=p.wait()
	return output.strip()

def get_pids():
	p=subprocess.Popen("pidof python", stdout=subprocess.PIPE, shell=True)
	(output,err)=p.communicate()
	p_status=p.wait()
	return output.split()

def kill(pid):
	os.system("kill -9 %s" % pid)

if len(sys.argv) < 3:
	print "usage:"
	print sys.argv[0], "<query pid>", "<magic_number>"
	sys.exit(0)

magic_number=sys.argv[2]

while 1:
	head=long(https_cnt())
	time.sleep(20*60*60)
	if head + long(magic_number) > long(https_cnt()):
		# lower than expect
		parr=get_pids()
		try:
			pid=str(os.getpid())
			parr.remove(sys.argv[1])
			parr.remove(pid)
		except:
			pass
		if len(parr) > 1:
			print "too many pythons to kill"
			break
		kill(parr[0])
