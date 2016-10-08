# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


# monthlist = ['1', '7', '8']
PTT_url = 'https://www.ptt.cc'
DEFAULT_URL = '/bbs/nb-shopping/index.html'


def pasrInside(inside_url):
    res = requests.get(inside_url, verify=True)
    soup = BeautifulSoup(res.text, "lxml")
    content = soup.find(id="main-content").text
    print content


def get_posts(url):
    nex_url = ''
    cur_url = '%s%s' % (PTT_url, url)
    print cur_url
    res = requests.get(cur_url, verify=True)
    # print res.text
    soup = BeautifulSoup(res.text, "lxml")
    prev = soup.findAll(True, {'class': 'btn wide'})[1]
    nex_url = prev.get('href')
    for entry in soup.select(".r-ent"):
        if entry.select('.title')[0].text[2].encode('utf-8') == '賣':
            print entry.select('.title')[0].text, \
                entry.select('.date')[0].text

    return nex_url


def parse_start():
    pages = 1
    nxt_rul = DEFAULT_URL
    while pages > 0:
        nxt_rul = get_posts(nxt_rul)
        pages = pages - 1


if __name__ == '__main__':
    parse_start()
