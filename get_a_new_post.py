from bs4 import BeautifulSoup
import urllib
import urllib2

url = 'http://www.yousuu.com/comments/digest'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
headers = { 'User-Agent' : user_agent }    
request = urllib2.Request(url)  
response = urllib2.urlopen(request)  
page = response.read() 

soup=BeautifulSoup(page)
backpage=str(soup.find("div","ys-comments-message"))

f=open('D:/t.txt','a')
f.write(backpage)
f.close()