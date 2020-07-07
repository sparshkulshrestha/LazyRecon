#!/usr/bin/python

import os
import sys
import subprocess
from multiprocessing import Process

def subdomain(domain):

	os.system("mkdir /root/pentest/targets/"+domain)  # create a directory
	subprocess.call("python /root/pentest/enumeration/Sublist3r/sublist3r.py -d %s -t 10 -v -o /root/pentest/targets/%s/sublist3r.txt" % (domain, domain), shell=True)
	subprocess.call("subfinder -d %s -silent -o /root/pentest/targets/%s/subfinder.txt" % (domain, domain), shell=True)
	os.system("curl -s https://crt.sh/?q=%25.{} |  grep {} | grep TD | sed -e 's/<//g' | sed -e 's/>//g' | sed -e 's/TD//g' | sed -e 's/\///g' | sed -e 's/ //g' | sed -n '1!p' | sort -u >> /root/pentest/targets/{}/certsh.txt".format(domain, domain, domain))  
	subprocess.call("/root/go/bin/./amass enum -d %s -o /root/pentest/targets/%s/amass.txt" % (domain, domain), shell=True)
	subprocess.call("cat /root/pentest/targets/%s/sublist3r.txt >> /root/pentest/targets/%s/merged.txt" % (domain, domain), shell=True)
	subprocess.call("cat /root/pentest/targets/%s/subfinder.txt >> /root/pentest/targets/%s/merged.txt" % (domain, domain), shell=True)
	subprocess.call("cat /root/pentest/targets/%s/certsh.txt >> /root/pentest/targets/%s/merged.txt" % (domain, domain), shell=True)
	subprocess.call("cat /root/pentest/targets/%s/amass.txt >> /root/pentest/targets/%s/merged.txt" % (domain, domain), shell=True)
	subprocess.call("sort /root/pentest/targets/%s/merged.txt | uniq >> /root/pentest/targets/%s/%s.txt" % (domain, domain, domain), shell=True)
	print("\n\n [!] Results are saved in /root/pentest/targets/{}/ \n\n".format(domain))
	return

def uphost(domain):  # find uphosts

	subprocess.call("cat /root/pentest/targets/%s/%s.txt | filter-resolved > /root/pentest/targets/%s/uphost-%s.txt" % (domain, domain, domain, domain), shell=True)
	subprocess.call("cat /root/pentest/targets/%s/uphost-%s.txt | httprobe > /root/pentest/targets/%s/alive.txt" % (domain, domain, domain), shell=True)
	return

def brute(domain):

	print("\n\n Performing Brute Force \n\n")
	subprocess.call("ffuf -w /root/pentest/wordlists/top1000.txt:DIR -w /root/pentest/targets/%s/alive.txt:SUB -u SUB/DIR -o /root/pentest/targets/%s/ffuf.out -of md -mc 200" % (domain,domain), shell=True)
	subprocess.call("cat /root/pentest/targets/%s/ffuf.out | cut -d \"|\" -f4 > /root/pentest/targets/%s/ffuf-final.out" % (domain,domain), shell=True)
	return

def vulns(domain):

	subprocess.call("cat /root/pentest/targets/%s/alive.txt | CORS-Scanner > /root/pentest/targets/%s/CORS-check.txt" % (domain,domain), shell=True) 
	return

def httpss(domain):  # take screenshots

	subprocess.call("python3 /root/pentest/enumeration/EyeWitness/EyeWitness.py --web -f /root/pentest/targets/%s/alive.txt --no-prompt -d /root/pentest/targets/%s/httpss" % (domain, domain), shell=True)
	return


def portscan(domain):  # portscanning using masscan

	os.system("massdns -r /root/pentest/portscan/massdns/lists/resolvers.txt -t A -o S -w /root/pentest/targets/{}/massdns.out /root/pentest/targets/{}/uphost-{}.txt".format(domain, domain, domain))
	os.system("cat /root/pentest/targets/{}/massdns.out | awk '{print $3}' | sort -u | grep -oE \"\b([0-9]{1,3}\.){3}[0-9]{1,3}\b\" > /root/pentest/targets/{}/ips-online.txt".format(domain, domain))
	os.system("masscan -iL /root/pentest/targets/{}/ips-online.txt --rate 10000 -p1-65535 --only-open -oL -oG /root/pentest/targets/{}/masscan.out".format(domain, domain))

def runInParallel(*fns):
	proc = []
	for fn in fns:
		p = Process(target=fn)
		p.start()
		proc.append(p)
	for p in proc:
		p.join()

def main():

	banner="""
   _     ____  ____ ___  _ ____  _____ ____ ____  _
 / \   /  _ \/_   \\  \///  __\/  __//   _Y  _ \/ \  /|
 | |   | / \| /   / \  / |  \/||  \  |  / | / \|| |\ ||
 | |_/\| |-||/   /_ / /  |    /|  /_ |  \_| \_/|| | \||
 \____/\_/ \|\____//_/   \_/\_\\____\\____|____/\_/  \|
 https://twitter.com/d0tdotslash"""

	print banner
	domain=sys.argv[1]
	print domain
	subdomain(domain)
	uphost(domain)
	runInParallel(brute(domain), httpss(domain))
	#portscan(domain)
	print banner

main()
