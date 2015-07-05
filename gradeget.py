#coding=utf-8

import urllib2
import urllib
from bs4 import BeautifulSoup

def main():
    url='http://www.yousuu.com/comments'
    response=urllib2.urlopen(url)
    soup=BeautifulSoup(response.read())
    tag=soup.find("span","num2star")
    grade=tag.get_text()
    return grade.encode('utf-8')