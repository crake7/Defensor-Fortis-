<h1 align="center"> Ethical Hacking: Tools and Malware</h1>
<h4 align="center">An assortment of tools and malware written in Python to use in a penetration test.</h4>

<p align="center">
  <a href="#How-to">How To</a> •
  <a href="#Requirements">Requirements</a> •
  <a href="#Tools">Tools</a> •
  <a href="#Credits">Credits</a>
</p>

___

<h4>Are you looking for some crafted tools to use during a penetration test?</h4>
<p>
The following programs have been created to learn how to exploit system weaknesses and vulnerabilities using Python 2.X and 3.X.
You may need to tweak the program depending on the version you want to run.  
</p>

If you are looking for additional tools written in Python 3, check out my other repo: [Network-Pen-Test-Tools](https://github.com/crake7/Network-Pen-Test-Tools)!

## How-to

Each folder is provided with a text file named ```howto.md``` which explains how to use each program in detail. 

* I recommend using Metasploitable to test the exploits. Download a virtual machine [here](https://sourceforge.net/projects/metasploitable/)



## Requirements

Some of these programs will require you to bypass HTTPS. I used <strong>sslstrip</strong> in order to achieve this, beware this will not work with websites that use HSTS.

<h4>BYPASS HTTPS</h4>

1. Make sure your iptables are flushed by typing in the terminal: `iptables --flush`

2. Become MITM: Use any of the programs in the folder [ARP Spoofer](/ARP%20Spoofer/arp_spoofy_cmmdlineargs.py)

3. Run SSL Strip (runs by default in port 10,000): `sslstrip`

4. Redirect packets from your computer from port 80 to SSL Strip: `iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000`

5. Run the program. 

## Tools

The repo is divided in several categories: <strong>Network Exploitation Tools</strong>, <strong>Web Application</strong>, and <strong>Malware</strong>:

|Folder Name|Category|Description|Requirements|
|:--------:|:--------:|:--------:|:--------:|
|ARP Spoofer| Network Exploitation| Redirects the flow of packets in a network, allowing to interecept data and become MITM.| N/A||
|Backdoor| Malware| Gives remote control over the system it gets executed on, allowing to access file system, execute system commands and download & upload files.|N/A||
|Code Injector| Network Exploitation| Injects code in intercepted HTML pages. | Requires you to become MITM.||
|Crawler| Web App/Bug Bounty| Discovers hidden paths on a target website.| N/A||
|DNS Spoofer| Network Exploitation| Redirects DNS requests, eg: redirects requests to from one domain to another.| Requires you to become MITM.||
|Key Logger| Malware| Records key-strikes and sends them to you by email.|N/A||
|MAC Changer| Network Exploitation| Changes your MAC Address to anything we want.|N/A||
|Malware| Malware| Several files that download a file and execute it on target system.|N/A||
|Network Scanner| Network Exploitation| Scans network and discovers the IP and MAC address of all connected clients.| Requires you to become MITM.||
|Packet Sniffer| Network Exploitation| Filters intercepted data and shows usernames, passwords, visited links.| Requires you to become MITM.||
|Replace Downloads| Network Exploitation| Recognizes when a target is downloading a file from an HTTP page and then replaces it on the fly.| Requires you to become MITM.||
|Trojan| Malware| Downloads a trojan to execute the reverse backdoor.|Requires you to control a web server.||
|Vulnerability Scanner| Network Exploitation| Scans a target website for weaknesses and produces a report with all findings.| N/A||


## Credits

This repo was created while taking the course: [Learn Python & Ethical Hacking From Scratch](https://www.udemy.com/course/learn-python-and-ethical-hacking-from-scratch) by Zaid Sabih. 

Writers and contributors take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.


## License

The code is licensed under the MIT License.
