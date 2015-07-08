#coding=utf-8
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import save

def main(x):
    url = 'http://www.yousuu.com/comments' #打开书评网页
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36"}#伪装浏览器
    request = urllib2.Request(url,headers=headers)#构造请求  
    response = urllib2.urlopen(request)  
    page = response.read()
    soup=BeautifulSoup(page)#交给beautifulsoup处理
    msg=[]
    url=[]
    for i in range(x):
        tag=soup.find("div","ys-comments-message")#获取书评内容的内容
        i=tag.get_text()
        tag['class']='getoverit'        
        if i>280:
            i=i[0:280]
	msg.append(i)
    for u in url:
        nu=soup.find(href=re.compile('/book/'))
        u='http://www.yousuu.com'+nu.get('href')
        del nu['href']
	url.append(u)
    return msg+url