#!Venv/bin python3
# -*- coding: utf-8 -*-

import csv
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

baseUrl = 'https://www.eprocurement.gov.cy'
url = baseUrl + '/epps/quickSearchAction.do?selectedItem=quickSearchAction.do%3Flatest%3Dtrue%26searchSelect%3D1&d-3680175-p=1&latest=true&searchSelect=1&T01_ps=100'
html = urlopen(url).read()
html = html.decode('utf-8')

soup = BeautifulSoup(html, features='html.parser')
T01 = soup.find(id='T01')
rows = T01.findAll('tbody')[0].findAll('tr')

now = datetime.datetime.utcnow()

usedIds = []
with open('eproc.csv', newline='', delimiter='|', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONE)
    for row in reader:
        usedIds.append(row[0])

with open('eproc.csv', 'a', newline='', delimiter='|', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
    for row in rows:
        data = []
        tds = row.findAll('td')
        archor = tds[1].findAll('a')[0]
        link = archor['href']
        id = link.split('=')[1]
        if id not in usedIds:
            data.append(id)
            data.append(now.isoformat())
            data.append(baseUrl + link)
            data.append(tds[2].text.strip())
            data.append(archor.text.strip())
            data.append(tds[3].findAll('img')[0]['title'])
            data.append(tds[4].text.strip())
            data.append(tds[5].text.strip())
            data.append(tds[6].text.strip())
            data.append(tds[7].text.strip())
            data.append(tds[8].text.strip())
            data.append(baseUrl + tds[9].findAll('a')[0]['href'])
            data.append(tds[11].text.strip())
            writer.writerow(data)