#coding=utf-8

import urllib2
import urllib
import save

def main(text):
    post_data = urllib.urlencode({'font' :'xihei', 'text' : text })#Î¢²©ÕıÎÄ+Î¢²©±êÇ©
    post_url = 'http://www.weishell.com/changweibo/'
    r=urllib2.urlopen(post_url, post_data)
    picture=eval(r.read())
    return picture["imgurl"]