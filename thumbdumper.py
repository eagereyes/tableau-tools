#!/usr/bin/python

# Extract all the thumbnails from a Tableau workbook in .twb or .twbx format.
# Thumbnails are dumped into a directory named after the workbook to avoid
# clutter
# 
# Usage: thumbdumper.py <filname.twbx> (or <filename.twb>)
#
# Copyright 2018 Robert Kosara <rkosara@me.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from sys import argv
from os import mkdir
from base64 import b64decode
from zipfile import ZipFile
import xml.etree.ElementTree as ET

def extractThumbs(twbname, file):
	mkdir(twbname)
	data = ET.fromstring(file.read())
	for thumb in data.findall('./thumbnails/thumbnail'):
		print thumb.attrib['name']
		with open(twbname + '/' + thumb.attrib['name'] + '.png', 'w') as png:
			png.write(b64decode(thumb.text))

filename = argv[1]
basename = '.'.join(filename.split('.')[:-1])
if filename.endswith('.twb'):
	with open(filename, 'r') as inFile:
		extractThumbs(basename, inFile)
elif filename.endswith('.twbx'):
	zip = ZipFile(filename, 'r')
	inFile = zip.open(basename+'.twb')
	extractThumbs(basename, inFile)
else:
	print "Please call with a twb or twbx file argument!"
