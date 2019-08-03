# LazyRecon

Subdomain discovery using Sublist3r, certspotter, crt.sh , censys and amass and Subdomain bruteforcing using Gobuster.

# About
This script is intended to automate your reconnaissance process in an organized fashion by performing the following:<br>

Create a folder with recon notes<br>
Grab subdomains using Sublist3r , crt.sh , censys , subfinder and amass.<br>
Subdomain bruteforcing using Gobuster.<br>
Resolve hosts using tomnonnom's filter-resolved.<br>
Take http screenshot using EyeWitness.<br>


# Requirements
This requires following Bug Bounty Hunting Tools in your ~/Downloads/recon/passive directory for script to work.<br>

https://github.com/aboul3la/Sublist3r<br>
https://github.com/subfinder/subfinder<br>
https://github.com/christophetd/censys-subdomain-finder<br>
https://github.com/OJ/gobuster<br>
https://github.com/OWASP/Amass<br>
https://github.com/tomnomnom/hacks/tree/master/filter-resolved<br>
https://github.com/FortyNorthSecurity/EyeWitness<br>
<b>Wordlist used:</b>https://github.com/assetnote/commonspeak2-wordlists

# Warning: 
This code was originally created for personal use for myself, so it's a bit messy and hopefully it'll be cleaned up with more features in a later release.

# Demo:

![](ezgif.com-resize.gif)

# Whats New:
new tool added : subfinder.<br>
Now it will also take screenshots of found subdomains.<br>
Now it will use crt.sh instead of certspotter.<br>

# Inspired by:
https://twitter.com/armaancrockroax <br>
https://twitter.com/nahamsec <br>
