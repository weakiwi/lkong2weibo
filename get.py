#coding=utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup

def main():
    url = 'http://www.yousuu.com/comments/digest' #打开书评网页
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36"}#伪装浏览器
    request = urllib2.Request(url,headers=headers)  
    response = urllib2.urlopen(request)  
    page = response.read()
    soup=BeautifulSoup(page)
    tag=soup.find("div","ys-comments-message")#获取书评内容的内容
    msg=tag.get_text()
    return msg
