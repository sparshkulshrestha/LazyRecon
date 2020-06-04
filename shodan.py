#!/usr/bin/env python

import os 
import sys
import subprocess

def gather_info(target):

	os.system("mkdir /home/sparsh/Documents/shodan-data/"+target)
	print "Query : ip_str,port,org,hostnames,http.title  Filter : ssl"
	subprocess.call("shodan search --fields ip_str,port,org,hostnames,http.title ssl:%s --color | tee /home/sparsh/Documents/shodan-data/%s/results-%s.txt" % (target, target, target),shell=True)
	print "Query : ip_str,port,org,hostnames,http.title  Filter : hostname"
	subprocess.call("shodan search --fields ip_str,port,org,hostnames,http.title hostname:%s --color | tee -a /home/sparsh/Documents/shodan-data/%s/results-%s.txt" % (target, target, target),shell=True)
	print "Query : ip_str,port,org,hostnames,http.title  Filter : ssl.cert.subject.cn"
	subprocess.call("shodan search --fields ip_str,port,org,hostnames,http.title ssl.cert.subject.cn:%s --color | tee -a /home/sparsh/Documents/shodan-data/%s/results-%s.txt" % (target, target, target),shell=True)

def main():

	target = sys.argv[1]
	gather_info(target)

main()
