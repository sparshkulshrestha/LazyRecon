#!/usr/bin/python

import os

def subdomain(domain):
	
	os.system("mkdir ~/Downloads/targets/"+domain)

	os.system("python ~/Downloads/dotdotslash/recon/passive/Sublist3r/sublist3r.py -d {} -t 10 -v -o ~/Downloads/targets/{}/sublist3r.txt".format(domain, domain))
	
	os.system("curl -s https://certspotter.com/api/v0/certs\?domain\={} |jq '.[].dns_names' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u >> /home/sparsh/Downloads/targets/{}/certspot.txt".format(domain, domain))
	
	os.system("python ~/Downloads/dotdotslash/recon/passive/censys-subdomain-finder/censys_subdomain_finder.py {} -o ~/Downloads/targets/{}/censys.txt".format(domain, domain))
	
	os.system("~/go/src/gobuster/./gobuster -m dns -t 50 -u {} -w /home/sparsh/Downloads/dotdotslash/commonspeak2-wordlists/subdomains/subdomains.txt -o /home/sparsh/Downloads/targets/{}/gobuster.txt".format(domain,domain))
	
	os.system("cat ~/Downloads/targets/{}/gobuster.txt | cut -d ':' -f2 | sort -u >> ~/Downloads/targets/{}/gobuster_final.txt".format(domain,domain))
	
	os.system("amass enum -d {} -o ~/Downloads/targets/{}/amass.txt".format(domain, domain))
	
	print("Commonspeak wordlist bruteforce completed-------------------------")
		
	print("All tools executed successfully------------------------------------")	

	print("Formatting begins /\/\/\/\/\/\/\------------------------------------")

	os.system("echo {} >> ~/Downloads/targets/{}/{}.txt".format(domain, domain, domain))
	
	#os.system("python ~/Downloads/dotdotslash/recon/passive/fdns.py ~/Downloads/targets/{}/{}.txt".format(domain, domain))
	
	os.system("mv ~/Desktop/{} ~/Downloads/targets/{}/{}.txt".format(domain, domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/{}.txt |cut -d ',' -f2 | sort -u >> ~/Downloads/targets/{}/fdns.txt".format(domain, domain, domain))
	
	os.system("rm /home/sparsh/Downloads/targets/{}/{}.txt".format(domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/sublist3r.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/certspot.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/censys.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/gobuster_final.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/fdns.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	os.system("cat ~/Downloads/targets/{}/amass.txt >> ~/Downloads/targets/{}/merged.txt".format(domain, domain))
	
	os.system("sort ~/Downloads/targets/{}/merged.txt | uniq >> ~/Downloads/targets/{}/{}.txt".format(domain, domain, domain))

	print("-----------------------Formatting Done-------------------------------")	

	print("------------Results are saved in specified folder--------------------")

	print("------------------Lazy Recon Execution Completed---------------------")
	
	return


#def uphost(domain):
	
	#os.system("cat ~/Downloads/targets/{}/{}.txt | filter-resolved > ~/Downloads/targets/{}/uphost-{}.txt".format(domain,domain,domain,domain))

	#return




def main():
	
	subdomain('ENTER TARGET DOMAIN')
	#uphost('ENTER TARGET DOMAIN')


main()



























