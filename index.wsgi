#coding=utf-8
import sae
import sae.kvdb
import send
import get
import sys
    
def app(environ,start_response):
    status = '200 OK'  
    response_headers = [('Content-type', 'text/html; charset=utf-8')]  
    start_response(status, response_headers) 
    kv=sae.kvdb.Client()
    msg=get.main()
    if msg==kv.get('msg'):
       return 'old'
    else:
    	send.main(msg)
    	kv.replace('msg',msg)
        return 'new'

application = sae.create_wsgi_app(app)
