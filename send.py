#coding=utf-8

import urllib2
import urllib

def main(text):
    access_token = 'your-access-token'
    post_data = urllib.urlencode({'access_token' : access_token, 'status' : text.encode('utf-8') })
    post_url = 'https://api.weibo.com/2/statuses/update.json'
    r = urllib2.urlopen(post_url, post_data);
    print r.read()

if __name__ == '__main__':
    main(text)
