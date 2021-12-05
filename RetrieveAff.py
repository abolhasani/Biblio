import requests
import urllib.request
import os, http.cookiejar
#from http.cookiejar import CookieJar
#from pybliometrics.scopus import AffiliationSearch
#import html2text

My_API = 'edd6e4a257fe776e49aecd85af37d99c'

url='https://www-scopus-com.ezp2.semantak.com/api/published-affiliation-history?authorId=7005310614'

#python concat string
#url = "htpps: sdfl;sdkjf    author_id=%s " % i
#Sleep between requests

r = requests.get(url, headers={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'fa-IR,fa;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'ezproxy=u7de0bnnYvmYMkI; ezproxyl=u7de0bnnYvmYMkI; ezproxyn=u7de0bnnYvmYMkI; SCSessionID=D18053B9E122F1D12D53A3F06545D48F.i-03ae4324ede5c6526; scopusSessionUUID=93ec9d95-7866-48a5-9; scopus.machineID=D18053B9E122F1D12D53A3F06545D48F.i-03ae4324ede5c6526; AWSELB=CB9317D502BF07938DE10C841E762B7A33C19AADB1B003252A5224D77F95F9FA3D3FE18DB3F8E4F54B0063B800CCE6EB125B7D052510BA32070D9964CEACBAE7C5777723B79F51544D3985DE2EA072FE6D9B9F6FA4; at_check=true; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; mbox=session#53ed277c95df4569a9073d153c9aee90#1638720437|PC#53ed277c95df4569a9073d153c9aee90.37_0#1701963377; s_pers=%20v8%3D1638718577215%7C1733326577215%3B%20v8_s%3DFirst%2520Visit%7C1638720377215%3B%20c19%3Dsc%253Asearch%253Adocument%2520searchform%7C1638720377225%3B%20v68%3D1638718574388%7C1638720377233%3B; s_sess=%20e41%3D1%3B%20s_cpc%3D1%3B%20s_cc%3Dtrue%3B; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=-2121179033%7CMCIDTS%7C18967%7CMCMID%7C69611186551512937194572772766930288151%7CMCAID%7CNONE%7CMCOPTOUT-1638725777s%7CNONE%7CMCCIDH%7C601914710%7CvVersion%7C5.3.0',
'Host': 'www-scopus-com.ezp2.semantak.com',
'If-Modified-Since': 'Sun, 05 Dec 2021 15:35:18 GMT',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
})
with open("response.txt", "w") as f:
    f.write(r.text)