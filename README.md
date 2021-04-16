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

## How-to

Each folder is provided with a text file named ```howto``` which explains how to use each program in detail. 
<p>
I recommend using Metasploitable to test the exploits. Download a virtual machine [here](https://sourceforge.net/projects/metasploitable/)

</p>

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
|------|--------|--------|--------|
|ARP Spoofer| Network Exploitation| Redirects the flow of packets in a network, allowing to interecept data and become MITM.| N/A||
|Backdoor| Malware| Gives remote control over the system it gets executed on, allowing to access file system, execute system commands and download & upload files.N/A|||
|Code Injector| Network Exploitation| Injects code in intercepted HTML pages. | Requires you to become MITM.||
|Crawler| Web App/Bug Bounty| Discovers hidden paths on a target website.| N/A||
|DNS Spoofer| Network Exploitation| Redirects DNS requests, eg: redirects requests to from one domain to another.| Requires you to become MITM.||
|Key Logger| Malware| Records key-strikes and sends them to us by email.|N/A||



## Credits

This repo was created while taking the course: [Learn Python & Ethical Hacking From Scratch](https://www.udemy.com/course/learn-python-and-ethical-hacking-from-scratch) by Zaid Sabih. 

Writers and contributors take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.

