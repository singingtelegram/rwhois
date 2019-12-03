#!/usr/bin/env python3
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import urllib

base_url = "https://viewdns.info/reversewhois/?q="
data = []

if __name__ == "__main__":
    query = urllib.parse.quote_plus(input("Please input your reverse WHOIS query: "))
    url = base_url + query
    opts = Options()
    opts.set_headless()
    browser = Firefox(options=opts)
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, features="html.parser")
    table = soup.findAll('table')[2]
    body = table.find('tbody')
    rows = body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [element.text.strip() for element in cols]
        data.append([element for element in cols if element])
    for i in range(4, len(data)):
        for j in range(0, len(data[i])):
            print("{:30}".format(data[i][j]), end='')
        print()
