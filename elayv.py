# -*- coding: utf-8 -*-
import socket
import httplib
import urllib
print " "
print " "
print " "
print " *****************************"
print " *****************************"
print " ***         ELAYV         ***"
print " *****************************"
print " *****************************"
print " "
print "Hedefe ait IP aralığında 80. porttan cevap veren IP adreslerini arar"
print " "
print "Örnek: 192.168.1.16 ile 192.168.1.34 arasındaki IP adresleri taramak için:"
print "IP adresi temelini girin: 192.168.1.1"
print "IP adresi aralığı başı: 16"
print "IP adresi aralığı sonu: 34"
print " "
print "Eleştiri ve hakaret dolu tweetleriniz için: @basaranalper"
print " "

net= raw_input("IP adresi temelini girin: ")
net1= net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net1[2]+a
st1 = int(raw_input("IP adresi aralığı başı: "))
en1 = int(raw_input("IP adresi aralığı sonu: "))
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