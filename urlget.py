#coding=utf-8
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

def main():
    url = 'http://www.yousuu.com/comments'
    response=urllib2.urlopen(url)
    page=response.read()
    soup=BeautifulSoup(page)
    msg=soup.find(href=re.compile('/book/'))
    bkurl='http://www.yousuu.com'+msg.get('href')
    return bkurl.encode('utf-8')
