#!/usr/bin/env python

import sys
import pycurl
import cStringIO
import re
import HTMLParser
import time
import random
from urllib import quote,unquote


from urlparse import urlparse, parse_qs

##

_project={}
_project['name']="Google Search Scrapper"
_project['version']="v0.0.1"

config={
		"biw": 1400, # default browser width(?)
		"bih": 606, # default browser height
		"searchFormat": "https://www.google.co.kr/search?q=%s&newwindow=1&biw=%d&bih=%d&ei=%s&start=%d&sa=N"
		}

##

if len(sys.argv) != 2:
	print _project['name'],_project['version']
	print sys.argv[0],"<search Query>"

##

def request(url):
	cbuf=cStringIO.StringIO()
	try:
		c=pycurl.Curl()
		c.setopt(c.URL, url)
		c.setopt(c.WRITEFUNCTION, cbuf.write)
		c.perform()
		return cbuf.getvalue()
	except pycurl.error, error:
		errno, errstr=error
		print "An error occurred : ", errstr

##

def extractHREF(buf):
	crawl="(?<=href(?i)=\").*?(?=\")"
	arr=re.findall(crawl,buf)
	uarr_tmp=set(arr)
	uarr=[]

	h=HTMLParser.HTMLParser()

	for data in uarr_tmp:
		uarr.append(h.unescape(data))
	
	return uarr


##

############### code from here

# ei init
resp=request("www.google.com")
uarr=extractHREF(resp)
nl=parse_qs(urlparse(uarr[0]).query)
ei=nl['ei']

for start in xrange(0,990,10): # get 1000 items
	# search
	searchURL=config['searchFormat']%(quote(sys.argv[1]), config['biw'], config['bih'], ei, start)
	resp=request(searchURL)
	
	print resp

	# refresh ei
	ei_tmp=ei
	ei=None
	uarr=extractHREF(resp)

	for i in range(len(uarr)):
		nl=parse_qs(urlparse(uarr[0]).query)
		try:
			ei=nl['ei']
			break
		except:
			ei=None

	if ei == None:
		print 'error here'
		break

	# sleep
	if start > 0 and start%50 == 0:
		time.sleep(15*60)
	else:
		time.sleep(random.uniform(1.5,5.5))
