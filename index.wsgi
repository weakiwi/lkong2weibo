#coding=utf-8
import sae
import ifkvdb
import send
import get
import sys
import shorturl
    
def app(environ,start_response):
    status = '200 OK'  
    response_headers = [('Content-type', 'text/html; charset=utf-8')]  
    start_response(status, response_headers) 
    response=get.main()
    surl=shorturl.main(response[2])
    msg=response[0]+surl
    return ifkvdb.main(msg)

application = sae.create_wsgi_app(app)