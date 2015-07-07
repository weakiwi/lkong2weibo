#coding=utf-8
import sae
import ifkvdb
import send
import get
import sys
import shorturl
import time
    
def app(environ,start_response):
    status = '200 OK'  
    response_headers = [('Content-type', 'text/html; charset=utf-8')]  
    start_response(status, response_headers) 
    response=get.main()
    surl1=shorturl.main(response[2])
    surl2=shorturl.main(response[3])
    msg1=response[0]+surl1
    msg2=response[1]+surl2
    ifkvdb.main(msg2)
    time.sleep(15)
    return ifkvdb.main(msg1)

application = sae.create_wsgi_app(app)