<h1 align="center"> Ethical Hacking: Tools and Malware</h1>
<h4 align="center">An assortment of tools and malware written in Python to use in a penetration test.</h4>

<p align="center">
  <a href="#Tools">Tools</a> •
  <a href="#Requirements">Requirements</a> •
  <a href="#Steps">Steps</a> •
  <a href="#Credits">Credits</a>
</p>

___


The following tools have been created to exploit system weaknesses and vulnerabilities using Python 2 and 3. 
(You may need to minimally tweak the program depending on the version you use.)  

Each folder is provided with a text file named "howto" which explains how to use each program in detail. 
In addition, some of these programs will require you to bypass HTTPS in order to maximize its utility.
I use "sslstrip" in order to achieve this, beware this will not work with websites that use HSTS.

BYPASS HTTPS
1. Make sure your iptables are flushed, type in bash terminal:
iptables --flush

2. Become MITM, you may use any of the progrmas in the folder ARP Spoofer.

3.Run SSL Strip, it runs by default in port 10,000. Type in terminal:
sslstrip

4. Redirect packets from your computer from port 80 to SSL Strip (again, on port 10,000). Type in terminal:
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000

5. Run the tool. 

Should you require any further guidance, feel free to contact me as well. 

I recommend using Metasploitable to test the exploits. 



Project created while taking the course: "Learn Python & Ethical Hacking From Scratch" by Zaid Sabih
