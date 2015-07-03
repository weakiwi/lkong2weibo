#coding=utf-8
from bs4 import BeautifulSoup
import urllib2
import urllib
import sae
import sae.kvdb


url = 'http://www.yousuu.com/comments/digest' #打开书评网页
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36"}#伪装浏览器
request = urllib2.Request(url,headers=headers)  
response = urllib2.urlopen(request)  
page = response.read()

soup=BeautifulSoup(page)
tag=soup.find("div","ys-comments-message")#获取书评内容的内容
msg=tag.get_text()
kv=sae.kvdb.Client()#kvdb服务初始化
kv.replace('newmsg',msg.encode('utf-8'))#将msg存放在新键值中

def main():
    if kv.get('newmsg')==kv.get('oldmsg'):#如果旧键值和新键值相同，则不发送
        return
    access_token = 'token'#你的token
    head={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36"}#伪装浏览器
    post_data = urllib.urlencode({'access_token' : access_token, 'status' : msg.encode('utf-8') })
    post_url = urllib2.Request('https://api.weibo.com/2/statuses/update.json',headers=head)
    r = urllib2.urlopen(post_url, post_data);
    bucket.delete_object('log.txt')
    kv.replace('oldmsg',msg.encode('utf-8'))
    

if __name__ == '__main__':
    main()
    
def app(environ,start_response):
    status = '200 OK'  
    response_headers = [('Content-type', 'text/html; charset=utf-8')]  
    start_response(status, response_headers) 
    main()
    return "hello"

application = sae.create_wsgi_app(app)
