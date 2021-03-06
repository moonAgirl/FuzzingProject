#!/usr/bin/python

#
# Copyright: Collin Mulliner <collin@mulliner.org>
# Web: http://www.mulliner.org/nfc/
#
# License: GPLv2
#
import time
def fromHex(v):
	b = int(v, 16)
	return b & 0xFF

def toHex(v, small = 0):
	ht = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	hts = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
	if small == 1:
		d1 = hts[v/16]
		d2 = hts[v%16]
	else:
		d1 = ht[v/16]
		d2 = ht[v%16]
	return d1 + d2

def bin2hex(data, chars = 0):
	o = ""
	for i in range(0, len(data)):
		if chars == 0:
			o = o + toHex(data[i])
		else:
			o = o + toHex(ord(data[i]))
	return o

def hex2bin(data, a = 1):
	if a == 1:
		raw_data = []
		for i in range(0, len(data) / 2):
			raw_data.append(fromHex(data[(i * 2)] + data[(i * 2) + 1]))
		return raw_data
	else:
		raw_data = ""
		for i in range(0, len(data) / 2):
			raw_data = raw_data + chr(fromHex(data[(i * 2)] + data[(i * 2) + 1]))
		return raw_data

def log_print(string):
    fid=open("log.txt",'a')
    fid.write(time.asctime()+":\t")
    fid.write(string+"\r\n")
    fid.close()
    print string

def log(string):
    log_print(string)
