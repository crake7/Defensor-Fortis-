#!/usr/bin/env python

import requests, re
# from urlparse import urljoin
import urllib.parse as urlparse
# def request(url):
#     try:
#         return requests.get("http://" + url)
#     except requests.exceptions.ConnectionError:
#         pass
#     except requests.exceptions.InvalidURL:
#         pass

target = "https://example.com"
links_list =[]

def extract_links(url):
   """#Extract all LINKS from page, we split the pattern (remove-word-?:)(non-greedy-?)"""
   response = requests.get(url)
# print(response.content)
   href_links = re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))
   return href_links

def crawl(url):
    """Read HTML page and create unique-value list with absolute URL's."""
    href_links = extract_links(url)
    for link in href_links:
        # link = urljoin(url, link)
        link = urlparse.urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]
        if target in link and link not in links_list:
            links_list.append(link)
            print(link)
            crawl(link)

# print(links_list)
crawl(target)