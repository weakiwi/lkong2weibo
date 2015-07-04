#coding=utf-8
import sae
import ifkvdb
import send
import get
import sys
import shorturl
import urlget
    
def app(environ,start_response):
    status = '200 OK'  
    response_headers = [('Content-type', 'text/html; charset=utf-8')]  
    start_response(status, response_headers) 
    kv=sae.kvdb.Client()
    surl=shorturl.main(urlget.main())
    msg=get.main()+surl
    return ifkvdb.main(msg)

application = sae.create_wsgi_app(app)
