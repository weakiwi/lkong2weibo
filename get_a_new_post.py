from bs4 import BeautifulSoup
import urllib
import urllib2
from weibo import APIClient

url = 'http://www.yousuu.com/comments/digest'   
request = urllib2.Request(url)  
response = urllib2.urlopen(request)  
page = response.read() 

soup=BeautifulSoup(page)
tag=soup.find("div","ys-comments-message")

APP_KEY = '1099528704'   
APP_SECRET = '326c042825bd4cc73dca4960979aedde'   
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'


def getclient():
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    auth_url = client.get_authorize_url()
    f=open("D:/t.txt","a")
    f.write(auth_url)
    f.close
    code = raw_input("input the retured code : ")  

    r = client.request_access_token(code)
    access_token = r.access_token
    expires_in = r.expires_in

    client.set_access_token(access_token, expires_in)

    return client

def posttext(client):
    utext = unicode(tag.get_text().encode('utf-8'), "UTF-8")
    client.statuses.update.post(status=utext)

if __name__ == '__main__':
     client = getclient()
     posttext(client)