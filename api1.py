import numpy
import requests
import urllib.request
import os, http.cookiejar
import pandas as pd

df = pd.read_csv('Data/Scopus-Author.csv', names=['Author Name', 'Auth-ID', 'Number of Documents', 'Subject Area', 'Orc_ID'], encoding='cp1252')
arr = df["Auth-ID"].to_numpy()
sizearr = arr.size

My_API = 'edd6e4a257fe776e49aecd85af37d99c'

urlcon='https://www-scopus-com.ezp2.semantak.com/api/published-affiliation-history?authorId='
print(sizearr)
for i in range(1, sizearr):
    print(i)
    defi = "ID="+str(arr[i])
    file_object = open('ReqResults/results.txt', 'a')
    file_object.write(str(i)+" out of "+str(sizearr)+":"+'\n'+defi+'\n')
    Author_ID = str(arr[i])
    r = requests.get(urlcon + Author_ID, headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'fa-IR,fa;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_sp_id.259a=26c1cb62-a815-4923-87fd-28a50f5e884c.1634219843.1.1634219852.1634219843.617968fa-78d8-4e0c-950a-9b62522e005c; _ga=GA1.2.504995989.1634219865; scopus.machineID=7AEB7BBBF8F9691C14E991289B9D8AF1.i-02185723b313690f9; ezproxy=6CaanmRK2kKSqUF; ezproxyl=6CaanmRK2kKSqUF; ezproxyn=6CaanmRK2kKSqUF; SCSessionID=4F7E7165DCCBE8DC8FD965FD2C7F431C.i-05049c12baa57ee80; scopusSessionUUID=4efbb9fe-cbdd-492f-8; AWSELB=CB9317D502BF07938DE10C841E762B7A33C19AADB14DAC630376FF0677501646DFF48E0B943BA74B5FE27D288D35A8ED487FE66C3ABAFDF2ADE925350150D7900CAD0CA8A6EF4666BB5B534D491844E1DC0DDF878D; at_check=true; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; mbox=PC#379c812622704f1a8d60bf353f9f25e4.37_0#1702840865|session#2bdbbcfe042444c3875e15f66c7d2d61#1639597925; s_pers=%20v8%3D1639596065381%7C1734204065381%3B%20v8_s%3DLess%2520than%25201%2520day%7C1639597865381%3B%20c19%3Dsc%253Asearch%253Aauthor%2520results%7C1639597865392%3B%20v68%3D1639596061231%7C1639597865411%3B; s_sess=%20s_cpc%3D0%3B%20s_ppvl%3Dsc%25253Arecord%25253Aaffiliation%252520details%252C59%252C42%252C1061%252C1536%252C761%252C1536%252C864%252C2.5%252CP%3B%20s_sq%3D%3B%20s_ppv%3Dsc%25253Asearch%25253Aauthor%252520results%252C25%252C25%252C1061%252C1536%252C761%252C1536%252C864%252C2.5%252CP%3B%20c21%3Dlastname%253Dbabol%2520noshirvani%2520university%2520of%2520technology%3B%20e13%3Dlastname%253Dbabol%2520noshirvani%2520university%2520of%2520technology%253A1%3B%20c13%3Ddocument%2520count%2520%2528high-low%2529%3B%20e41%3D1%3B%20s_cc%3Dtrue%3B; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=-2121179033%7CMCIDTS%7C18977%7CMCMID%7C08521765806907916934556290735525227426%7CMCAID%7CNONE%7CMCOPTOUT-1639603265s%7CNONE%7CvVersion%7C5.3.0%7CMCCIDH%7C601914710%7CMCAAMLH-1637492026%7C6%7CMCAAMB-1639589852%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI',
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
    file_object.write('\n'+'\n')
    file_object.close()

print("Task Finished")