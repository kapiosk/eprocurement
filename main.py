#!Venv/bin python3
# -*- coding: utf-8 -*-

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.eprocurement.gov.cy/epps/quickSearchAction.do?selectedItem=quickSearchAction.do%3Flatest%3Dtrue%26searchSelect%3D1&d-3680175-p=1&latest=true&searchSelect=1&T01_ps=100'
html = urlopen(url).read()
html = html.decode('utf-8')

soup = BeautifulSoup(html, features='html.parser')
T01 = soup.find(id='T01')
rows = T01.findAll('tbody')[0].findAll('tr')

for row in rows:
    tds = row.findAll('td')
    link = tds[1]
    cat = tds[2] 
    desc = tds[3] 
    pdate = tds[4] 
    ddate = tds[5] 
    status = tds[6] 
    stat2 = tds[7] 
    stat3 = tds[8] 
    link2 = tds[9] 
    price = tds[11]