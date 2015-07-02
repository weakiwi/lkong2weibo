from bs4 import BeautifulSoup
import urllib
import urllib2

url = 'http://www.yousuu.com/comments/digest' #打开书评网页  
request = urllib2.Request(url)  
response = urllib2.urlopen(request)  
page = response.read() 

soup=BeautifulSoup(page)
tag=soup.find("div","ys-comments-message")#获取指定标签的内容

def main():	
	msg = tag.get_text()

	access_token = '2.00JVt9uBwdV6MB2549560a41PkrEgB'#你的access_token，可以通过http://open.weibo.com/tools/console获取
	post_data = urllib.urlencode({'access_token' : access_token, 'status' : msg.encode('utf-8') })

	post_url = 'https://api.weibo.com/2/statuses/update.json'
	r = urllib2.urlopen(post_url, post_data);
	print r.read()

if __name__ == '__main__':
	main()