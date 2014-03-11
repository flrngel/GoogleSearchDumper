#!/usr/bin/env python

import sys
import cStringIO
import re
import HTMLParser
from urlparse import urlparse, parse_qs

def extractHREF(buf):
	crawl="(?<=href(?i)=\"/url\?q=).*?(?=\")"
	arr=re.findall(crawl,buf)
	uarr_tmp=set(arr)
	uarr=[]

	h=HTMLParser.HTMLParser()

	for data in uarr_tmp:
		uarr.append(h.unescape(data))
	
	return uarr

f=file(sys.argv[1])
s=f.read()

xresult=extractHREF(s)
sresult=[]

for data in xresult:
	res=urlparse(data)
	if res.scheme == 'https' :
		sresult.append(res.netloc)

result=set(sresult)

for data in result:
	splited=data.split(":")
	if len(splited) > 1 :
		print splited[0], splited[1]
	else:
		print splited[0]
