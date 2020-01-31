#!/usr/bin/python

import os
import sys
import subprocess

def subdomain(domain):

        os.system("mkdir /root/pentest/targets/"+domain)  #create a directory

        os.system("python /root/pentest/enumeration/Sublist3r/sublist3r.py -d {} -t 10 -v -o /root/pentest/targets/{}/sublist3r.txt".format(domain, domain)) #run sublist3r tool #1

        os.system("/root/pentest/enumeration/./subfinder -d {} -silent -o /root/pentest/targets/{}/subfinder.txt".format(domain, domain)) #run subfinder tool #2

        os.system("curl -s https://crt.sh/?q=%25.{} |  grep {} | grep TD | sed -e 's/<//g' | sed -e 's/>//g' | sed -e 's/TD//g' | sed -e 's/\///g' | sed -e 's/ //g' | sed -n '1!p' | sort -u >> /root/pentest/targets/{}/certsh.txt".format(domain, domain, domain)) #grep subdomains from crt.sh tool #3

        os.system("python /root/pentest/enumeration/censys-subdomain-finder/censys_subdomain_finder.py {} -o /root/pentest/targets/{}/censys.txt".format(domain, domain)) #run censys tool #4

        os.system("/root/go/bin/./gobuster -m dns -t 50 -u {} -w /root/pentest/wordlists/commonspeak2-wordlists/subdomains/subdomains.txt -o /root/pentest/targets/{}/gobuster.txt".format(domain,domain)) #run gobuster tool #5

        os.system("cat /root/pentest/targets/{}/gobuster.txt | cut -d ' ' -f2 | sort -u >> /root/pentest/targets/{}/gobuster_final.txt".format(domain,domain)) #sort gobuster.txt

        os.system("/root/go/bin/./amass enum -d {} -o /root/pentest/targets/{}/amass.txt".format(domain, domain)) #run amass tool #6

        os.system("echo {} >> /root/pentest/targets/{}/{}.txt".format(domain, domain, domain))

        #os.system("python /root/pentest/enumeration/fdns.py /root/pentest/targets/{}/{}.txt".format(domain, domain))

        #os.system("mv ~/Desktop/{} /root/pentest/targets/{}/{}.txt".format(domain, domain, domain))

        os.system("cat /root/pentest/targets/{}/{}.txt |cut -d ',' -f2 | sort -u >> /root/pentest/targets/{}/fdns.txt".format(domain, domain, domain))

        os.system("rm /root/pentest/targets/{}/{}.txt".format(domain, domain))

        os.system("cat /root/pentest/targets/{}/sublist3r.txt >> /root/pentest/targets/{}/merged.txt".format(domain, domain))

        os.system("cat /root/pentest/targets/{}/subfinder.txt >> /root/pentest/targets/{}/merged.txt".format(domain, domain))

        os.system("cat /root/pentest/targets/{}/certsh.txt >> /root/pentest/targets/{}/merged.txt".format(domain, domain))

        os.system("cat /root/pentest/targets/{}/censys.txt >> /root/pentest/targets/{}/merged.txt".format(domain, domain))

        os.system("cat /root/pentest/targets/{}/gobuster_final.txt >> /root/pentest/targets/{}/merged.txt".format(domain, domain))

        os.system("cat /root/pentest/targets/{}/fdns.txt >> /root/pentest/targets/{}/merged.txt".format(domain, domain))

        os.system("cat /root/pentest/targets/{}/amass.txt >> /root/pentest/targets/{}/merged.txt".format(domain, domain))

        os.system("sort /root/pentest/targets/{}/merged.txt | uniq >> /root/pentest/targets/{}/{}.txt".format(domain, domain, domain))

        print("\n\n [!] Results are saved in /root/pentest/targets/{}/ \n\n".format(domain))

        return


def uphost(domain): #find uphosts

        os.system("cat /root/pentest/targets/{}/{}.txt | filter-resolved > /root/pentest/targets/{}/uphost-{}.txt".format(domain,domain,domain,domain))         #tomnomnom's filter-resolved
        os.system("cat /root/pentest/targets/{}/uphost-{}.txt | httprobe > /root/pentest/targets/{}/alive.txt".format(domain,domain,domain))                    #tomnomnom's httprobe
        return


def httpss(domain): #take screenshots

        os.system("python3 /root/pentest/enumeration/EyeWitness/EyeWitness.py --web -f /root/pentest/targets/{}/alive.txt --no-prompt -d /root/pentest/targets/{}/httpss".format(domain,domain))

        return


def portscan(domain):   #portscanning using masscan

        os.system("massdns -r /root/pentest/portscan/massdns/lists/resolvers.txt -t A -o S -w /root/pentest/targets/{}/massdns.out /root/pentest/targets/{}/uphost-{}.txt".format(domain,domain,domain))
        os.system("cat /root/pentest/targets/paytm.com/massdns.out | cut -f3 | sed -n '/\(\(1\?[0-9][0-9]\?\|2[0-4][0-9]\|25[0-5]\)\.\)\{3\}\(1\?[0-9][0-9]\?\|2[0-4][0-9]\|25[0-5]\)/p' | cut -d \" \" -f3| sort -u > /root/pentest/targets/{}/ips-online.txt".format(domain))
        os.system("sudo masscan -iL /root/pentest/targets/{}/ips-online.txt --rate 10000 -p1-65535 -oL /root/pentest/targets/{}/masscan.out".format(domain,domain))


#def slackbot():

#       slack=""
#       message=":)"
#       slack.chat.post_message('#general',message);

#       uphost_file = {

#               'file' : ('/root/pentest/targets/{}/uphost-{}.txt',open('/root/pentest/targets/{}/uphost-{}.txt'
#        return


def main():

        banner =  """ 
   _     ____  ____ ___  _ ____  _____ ____ ____  _
 / \   /  _ \/_   \\  \///  __\/  __//   _Y  _ \/ \  /|
 | |   | / \| /   / \  / |  \/||  \  |  / | / \|| |\ ||
 | |_/\| |-||/   /_ / /  |    /|  /_ |  \_| \_/|| | \||
 \____/\_/ \|\____//_/   \_/\_\\____\\____|____/\_/  \|
 https://twitter.com/d0tdotslash"""

        print banner
        domain = sys.argv[1]
        print domain
        subdomain(domain)
        uphost(domain)
        httpss(domain)
        #portscan(domain)
        print banner
        print ("\nfiles to be reviewed : uphost-{}.txt, httpss dir, masscan.out\n".format(domain)) 

main()
