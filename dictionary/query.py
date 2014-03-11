#!/usr/bin/env python

#-*- coding: utf-8 -*-

import sys
from subprocess import call

f=file("dict.txt");
lines=f.readlines()

for line in lines:
	argv="inurl:https inurl:co.kr "+line.strip()
	call(["../bot.py",argv])
