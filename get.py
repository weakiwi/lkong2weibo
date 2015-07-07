#coding=utf-8
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

def main():
    url = 'http://www.yousuu.com/comments' #打开书评网页
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36"}#伪装浏览器
    request = urllib2.Request(url,headers=headers)#构造请求  
    response = urllib2.urlopen(request)  
    page = response.read()
    soup=BeautifulSoup(page)#交给beautifulsoup处理
    tag=soup.find("div","ys-comments-message")#获取书评内容的内容
    tag['class']='getoverit'
    tag1=soup.find("div","ys-comments-message")
    gradetag=soup.find("span","num2star")
    grade=gradetag.get_text()
    msg=tag.get_text()
    msg1=tag1.get_text()
    url1=soup.find(href=re.compile('/book/'))
    skurl1=url1.get('href')
    del url1['href']
    url2=soup.find(href=re.compile('/book/'))
    skurl2=url2.get('href')
    bkurl1='http://www.yousuu.com'+skurl1
    bkurl2='http://www.yousuu.com'+skurl2
    if msg>280:
        msg=msg[0:280]
    if msg1>280:
        msg1=msg1[0:280]
    return [msg.encode('utf-8'),msg1.encode('utf-8'),bkurl1,bkurl2]
