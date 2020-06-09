#!/usr/bin/env python

import os 
import sys
import subprocess

def gather_info(target):

	os.system("mkdir /home/sparsh/Documents/shodan-data/"+target)
	print "Query : ip_str,port,org,hostnames,http.title  Filter : ssl"
	subprocess.call("shodan search --fields ip_str,port,org,hostnames,http.title ssl:%s --color | tee ~/Documents/shodan-data/%s/results-%s.txt" % (target, target, target),shell=True)
	print "Query : ip_str,port,org,hostnames,http.title  Filter : hostname"
	subprocess.call("shodan search --fields ip_str,port,org,hostnames,http.title hostname:%s --color | tee -a ~/Documents/shodan-data/%s/results-%s.txt" % (target, target, target),shell=True)
	print "Query : ip_str,port,org,hostnames,http.title  Filter : ssl.cert.subject.cn"
	subprocess.call("shodan search --fields ip_str,port,org,hostnames,http.title ssl.cert.subject.cn:%s --color | tee -a ~/Documents/shodan-data/%s/results-%s.txt" % (target, target, target),shell=True)

def scan(target):

	print "Unique IPs :" #formatting on found data to extract unique IPs
	os.system("cat ~/Documents/shodan-data/{}/results-{}.txt | awk {{'print $1'}} | sort -u | tee /home/sparsh/Documents/shodan-data/{}/ips-{}.txt".format(target,target,target,target))
	print "Query : Host " #in-depth scan for unique IPs
	subprocess.call("cat ~/Documents/shodan-data/%s/ips-%s.txt | while read line; do shodan host \"$line\"; done | tee -a ~/Documents/shodan-data/%s/portscan-%s.txt" % (target, target, target, target),shell=True)

def open_ports(targets):
	print "Open Ports"


def main():

	target = sys.argv[1]
	gather_info(target)
	scan(target)

main()
