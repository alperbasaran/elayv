#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import httplib
import urllib
import argparse

parser=argparse.ArgumentParser(description='Hedefe ait IP aralığında 80. porttan cevap veren IP adreslerini arar.')
parser.add_argument('-ip',type=str,help='IP adresi temeli', required=True)
parser.add_argument('-b',type=int,help='IP araligi basi', default=1)
parser.add_argument('-s',type=int,help='IP araligi sonu',default=255)

print " "
print " *****************************"
print " *****************************"
print " ***         ELAYV         ***"
print " *****************************"
print " *****************************"
print " "
print "Hedefe ait IP aralığında 80. porttan cevap veren IP adreslerini arar"
print " "
print "Örnek:192.168.1.16 ile 192.168.1.34 arasındaki IP adresleri taramak için:"
print "elayv.py -ip 192.168.1.1 -b 16 -s 34"
print " "
print "Eleştiri ve hakaret dolu tweetleriniz için: @basaranalper"
print " "

cmdargs=parser.parse_args()
net=cmdargs.ip
st1=cmdargs.b
en1=cmdargs.s

net1= net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
en1=en1+1
socket.setdefaulttimeout(3)

def scan(addr):
	try:
		conn = httplib.HTTPConnection(addr, 80)
		conn.request("GET", "/ HTTP/1.1")
		response = conn.getresponse() 
		print addr, "Burada bir şey olabilir: ", response.status 

	except (httplib.HTTPException, socket.error) as ex:
   		print addr, "Burada bir şey yok: %s" % ex
	
def run1():
	for ip in xrange(st1,en1):
		addr = net2+str(ip)
		if (scan(addr)):
			print addr 
run1()