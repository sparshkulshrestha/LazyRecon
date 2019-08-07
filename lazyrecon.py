#!/usr/bin/python

import os
import sys

def subdomain(domain):
	
	os.system("mkdir ~/Downloads/targets/"+domain)

	os.system("python ~/Downloads/recon/passive/Sublist3r/sublist3r.py -d {} -t 10 -v -o ~/Downloads/targets/{}/sublist3r.txt".format(domain, domain))
	
	os.system("~/Downloads/recon/passive/subfinder/./subfinder -d {} -silent -o ~/Downloads/targets/{}/subfinder.txt".format(domain, domain))
	
	os.system("curl -s https://crt.sh/?q=%25.{} |  grep {} | grep TD | sed -e 's/<//g' | sed -e 's/>//g' | sed -e 's/TD//g' | sed -e 's/\///g' | sed -e 's/ //g' | sed -n '1!p' | sort -u  >> /home/sparsh/Downloads/targets/{}/certspot.txt".format(domain, domain))
	
	os.system("python ~/Downloads/recon/passive/censys-subdomain-finder/censys_subdomain_finder.py {} -o ~/Downloads/targets/{}/censys.txt".format(domain, domain))
	
	os.system("~/go/src/gobuster/./gobuster -m dns -t 50 -u {} -w ~/Downloads/commonspeak2-wordlists/subdomains/subdomains.txt -o ~/Downloads/targets/{}/gobuster.txt".format(domain,domain))
	
	os.system("cat ~/Downloads/targets/{}/gobuster.txt | cut -d ':' -f2 | sort -u >> ~/Downloads/targets/{}/gobuster_final.txt".format(domain,domain))
	
	os.system("amass enum -d {} -o ~/Downloads/targets/{}/amass.txt".format(domain, domain))
	
	print("\n\n-----------------Commonspeak wordlist bruteforce completed-------------------------\n\n")
		
	print("\n\n---------------------All tools executed successfully---------------------------------\n\n")	

	print("\n\n-------------------------Formatting begins --------------------------------\n\n")

	os.system("echo {} >> ~/Downloads/targets/{}/{}.txt".format(domain, domain, domain))
	
	#os.system("python ~/Downloads/recon/passive/fdns.py ~/Downloads/targets/{}/{}.txt".format(domain, domain))
	
	#os.system("mv ~/Desktop/{} ~/Downloads/targets/{}/{}.txt".format(domain, domain, domain))
	
	#os.system("cat ~/Downloads/targets/{}/{}.txt |cut -d ',' -f2 | sort -u >> ~/Downloads/targets/{}/fdns.txt".format(domain, domain, domain))
	
	#os.system("rm ~/Downloads/targets/{}/{}.txt".format(domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/sublist3r.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/subfinder.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/certspot.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/censys.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/gobuster_final.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	#os.system("cat ~/Downloads/targets/{}/fdns.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/amass.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	os.system("sort ~/Downloads/targets/{}/merged.txt | uniq >> ~/Downloads/targets/{}/{}.txt".format(domain, domain, domain))

	print("\n\n-----------------------Formatting Done-------------------------------\n\n")	

	print("\n\n------------Results are saved in specified folder--------------------\n\n")

	print("\n\n------------------Lazy Recon Execution Completed---------------------\n\n")
	
	return


def uphost(domain):
	
	os.system("cat ~/Downloads/targets/{}/{}.txt | filter-resolved > ~/Downloads/targets/{}/uphost-{}.txt".format(domain,domain,domain,domain))

	return

def httpss(domain): #take screenshots

	os.system("python ~/Downloads/recon/passive/EyeWitness/EyeWitness.py --web -f ~/Downloads/targets/{}/uphost-{}.txt -d ~/Downloads/targets/{}/httpss".format(domain,domain,domain))

	return


def main():
	
		
	banner =  """ 
   _     ____  ____ ___  _ ____  _____ ____ ____  _
 / \   /  _ \/_   \\  \///  __\/  __//   _Y  _ \/ \  /|
 | |   | / \| /   / \  / |  \/||  \  |  / | / \|| |\ ||
 | |_/\| |-||/   /_ / /  |    /|  /_ |  \_| \_/|| | \||
 \____/\_/ \|\____//_/   \_/\_\\____\\____|____/\_/  \|
 https://twitter.com/d0tdotslash"""
	
	print banner
	print ("\n\n Usage : python lazyrecon.py\n\n")
	domain = sys.argv[1]
	print domain
	subdomain(domain)
	uphost(domain)
	print banner

main()


























