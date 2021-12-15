import numpy
import requests
import urllib.request
import os, http.cookiejar
import pandas as pd
#from http.cookiejar import CookieJar
#from pybliometrics.scopus import AffiliationSearch
#import html2text

df = pd.read_csv('Data/Scopus-Author.csv', names=['Author Name', 'Auth-ID', 'Number of Documents', 'Subject Area', 'Orc_ID'], encoding='cp1252')
arr = df["Auth-ID"].to_numpy()
sizearr = arr.size

My_API = 'edd6e4a257fe776e49aecd85af37d99c'
Author_ID = "7005310614"

urlcon='https://www-scopus-com.ezp2.semantak.com/api/published-affiliation-history?authorId='
#url = 'https://www-scopus-com.ezp2.semantak.com/api/published-affiliation-history?authorId=7005310614'
#url = urlcon + Author_ID

#python concat string
#url = "htpps: sdfl;sdkjf    author_id=%s " % i
#Sleep between requests

for i in range(1, sizearr):
    defi = "ID="+str(arr[i])
    file_object = open('resdata.txt', 'a')
    file_object.write(defi)
    file_object.write('\n')
    Author_ID = str(arr[i])
    r = requests.get(urlcon + Author_ID, headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'fa-IR,fa;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_sp_id.259a=26c1cb62-a815-4923-87fd-28a50f5e884c.1634219843.1.1634219852.1634219843.617968fa-78d8-4e0c-950a-9b62522e005c; _ga=GA1.2.504995989.1634219865; scopus.machineID=7AEB7BBBF8F9691C14E991289B9D8AF1.i-02185723b313690f9; mbox=PC#379c812622704f1a8d60bf353f9f25e4.37_0#1701961490|session#76c819b778424eb9a00497ebf0d0a503#1638718550; s_pers=%20c19%3Dsc%253Arecord%253Aauthor%2520details%7C1638718488497%3B%20v68%3D1638716684401%7C1638718488512%3B%20v8%3D1638716694623%7C1733324694623%3B%20v8_s%3DLess%2520than%25207%2520days%7C1638718494623%3B; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=-2121179033%7CMCIDTS%7C18967%7CMCMID%7C08521765806907916934556290735525227426%7CMCAID%7CNONE%7CMCOPTOUT-1638723894s%7CNONE%7CvVersion%7C5.3.0%7CMCCIDH%7C601914710%7CMCAAMLH-1637492026%7C6%7CMCAAMB-1638716639%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; ezproxy=6CaanmRK2kKSqUF; ezproxyl=6CaanmRK2kKSqUF; ezproxyn=6CaanmRK2kKSqUF; SCSessionID=4F7E7165DCCBE8DC8FD965FD2C7F431C.i-05049c12baa57ee80; scopusSessionUUID=4efbb9fe-cbdd-492f-8; AWSELB=CB9317D502BF07938DE10C841E762B7A33C19AADB14DAC630376FF0677501646DFF48E0B943BA74B5FE27D288D35A8ED487FE66C3ABAFDF2ADE925350150D7900CAD0CA8A6EF4666BB5B534D491844E1DC0DDF878D',
    'Host': 'www-scopus-com.ezp2.semantak.com',
    'If-Modified-Since': 'Wed, 15 Dec 2021 17:07:19 GMT',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    })
    file_object.write(r.text)
    file_object.write('\n')
    file_object.close()




#with open("response.txt", "w") as f:
#    f.write(r.text)