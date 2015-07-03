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
    return 'ok'
    kv=sae.kvdb.Client()
    msg=get.main()
    if msg==kv.get('msg'):
       sys.exit(0)
    send.main(msg)
    kv.set('msg',msg)  

application = sae.create_wsgi_app(app)
