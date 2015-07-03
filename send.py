#coding=utf-8

import urllib2
import urllib

def main(text):
    access_token = 'access_token1'
    access_token1='access_token2'
    post_data = urllib.urlencode({'access_token' : access_token, 'status' : text.encode('utf-8') })
    post_url = 'https://api.weibo.com/2/statuses/update.json'
    try:
        urllib2.urlopen(post_url, post_data)
    except urllib2.HTTPError, e:
        post_data1 = urllib.urlencode({'access_token' : access_token1, 'status' : text.encode('utf-8') })
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36')
        urllib2.urlopen(post_url, post_data1)
        print e.code
        print e.reason
    print 'ok';
        
if __name__ == '__main__':
    main(text)
