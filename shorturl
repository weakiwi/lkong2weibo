#coding=utf-8

import urllib2
import urllib

def main(longurl):
    source='sina_app_key'
    url_long=longurl
    post_data=urllib.urlencode({'source':source,'url_long':url_long})
    post_url='http://api.t.sina.com.cn/short_url/shorten.json'
    r=urllib2.urlopen(post_url, post_data)
    shorturl=r.read()
    shorturl=shorturl[15:45]
    step=0
    for i in shorturl:
        if i=='\"':
            break
        step=step+1
    return shorturl[0:step]
