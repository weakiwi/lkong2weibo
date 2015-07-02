#coding=utf-8
from bs4 import BeautifulSoup
import urllib2
import urllib
import sae
import re

#coding=utf-8
from bs4 import BeautifulSoup
import urllib2
import urllib

url = 'http://www.yousuu.com/comments/digest' #打开书评网页
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36"}#伪装浏览器方位
request = urllib2.Request(url,headers=headers)  
response = urllib2.urlopen(request)  
page = response.read()



soup=BeautifulSoup(page)
tag=soup.find("div","ys-comments-message")#获取书评内容的内容
time=soup.find("div","media-body")#
mode=re.compile(r'\d+')
temp=time.get_text()
x=mode.findall(str(temp.encode('utf-8')))#提取书评内容中的两个数字构成列表，其中第一个为“x分钟前”的x，第二个元素为书籍评分
if x[0]<'60':#判断得到列表的第一位是不是合法时间（某些用户名包含数字）
    if x[0]<10 :#如果时间小于10分钟，则a=1
        a=1
    else :
        a=0
else:
    if x[1] < '10' :#如果第一位不是时间，开始匹配列表第二个元素
        a=1
    else:
        a=0    
   
def main():
    msg=tag.get_text()
    if a==0 :#大于十分钟说明微博已经发过，退出函数
        return
    access_token = '2.00JVt9uBwdV6MB2549560a41PkrEgB'
    post_data = urllib.urlencode({'access_token' : access_token, 'status' : msg.encode('utf-8') })
    post_url = 'https://api.weibo.com/2/statuses/update.json'
    r = urllib2.urlopen(post_url, post_data);
    
    
if __name__ == '__main__':
    main()
    
def app(environ,start_response):
    status = '200 OK'  
    response_headers = [('Content-type', 'text/html; charset=utf-8')]  
    start_response(status, response_headers) 
    main()
    return "GET IT!"

application = sae.create_wsgi_app(app)