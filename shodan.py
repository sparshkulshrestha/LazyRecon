#!/usr/bin/env python

import os 
import sys

def gather_info(target):

	os.system("mkdir /home/sparsh/Documents/shodan-data/"+target)
	print "Query : ip_str,port,org,hostnames,http.title  Filter : ssl"
	os.system("shodan search --fields ip_str,port,org,hostnames,http.title ssl:{} --color | tee /home/sparsh/Documents/shodan-data/{}/results-{}.txt".format(target,target,target))
	print "Query : ip_str,port,org,hostnames,http.title  Filter : hostname"
	os.system("shodan search --fields ip_str,port,org,hostnames,http.title hostname:{} --color | tee -a /home/sparsh/Documents/shodan-data/{}/results-{}.txt".format(target,target,target))
	print "Query : ip_str,port,org,hostnames,http.title  Filter : ssl.cert.subject.cn"
	os.system("shodan search --fields ip_str,port,org,hostnames,http.title ssl.cert.subject.cn:{} --color | tee -a /home/sparsh/Documents/shodan-data/{}/results-{}.txt".format(target,target,target))

def formatting(target):

	print "Unique IPs :"
	os.system("cat /home/sparsh/Documents/shodan-data/{}/results-{}.txt | awk {{'print $1'}} | sort -u | tee /home/sparsh/Documents/shodan-data/{}/ips-{}.txt".format(target,target,target,target))
	print "Taking Screenshot of Found Hosts :"
	os.system("cat /home/sparsh/Documents/shodan-data/{}/results-{}.txt | awk {{'print $1,$2'}} | sort -u | sed 's/ /:/' | tee /home/sparsh/Documents/shodan-data/{}/hosts-{}.txt".format(target,target,target,target))
	#os.system("python3 /root/pentest/enumeration/EyeWitness/EyeWitness.py -f /home/sparsh/Documents/shodan-data/{}/hosts-{}.txt".format(target,target))

def open_ports(targets):
	print "Open Ports"


def main():

	target = sys.argv[1]
	gather_info(target)
	formatting(target)

main()
