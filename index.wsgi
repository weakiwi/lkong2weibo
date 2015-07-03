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
    kv=sae.kvdb.Client()#kvdb服务初始化
    msg=get.main()#获取最新书评
    if msg==kv.get('msg'):#判断最新书评是否发布
       return 'an old massage'+str(msg.encode('utf-8'))#返回书评，方便抓虫
    else:
    	send.main(msg)#未发送则发送
    	kv.replace('msg',msg)
        return 'a new massage'+str(msg.encode('utf-8'))

application = sae.create_wsgi_app(app)
