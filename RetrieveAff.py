import requests
import urllib.request
#from http.cookiejar import CookieJar
import os, http.cookiejar
#from pybliometrics.scopus import AffiliationSearch
#import html2text

#print("Hello World");

#r = requests.get('https://www-scopus-com.ezp2.semantak.com/api/published-affiliation-history?authorId=7004834165&_=1638348886668')

My_API = 'edd6e4a257fe776e49aecd85af37d99c'

url='https://www-scopus-com.ezp2.semantak.com/api/published-affiliation-history?authorId=7005310614'
#urllib.request.urlretrieve(url, "test.txt")



#page = urllib.request.urlopen(url)
#html_content = page.read()
#rendered_content = html2text.html2text(html_content)
#file = open('file_text.txt', 'w')
#file.write(rendered_content)
#file.close()

#query = "AFFIL(Max Planck Institute for Innovation and Competition Munich)"
#s = AffiliationSearch(query)
#print(s)
#print(s.affiliations)

cj = http.cookiejar.MozillaCookieJar('Cookie.txt')
cj.load()
r = requests.get(url, cookies=cj)

with open("response.txt", "w") as f:
    f.write(r.text)