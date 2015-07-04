#coding=utf-8
import sae.kvdb

def main(msg):
    kv=sae.kvdb.Client()
    if msg==kv.get('msg'):
        return 'an old massage'+str(msg.encode('utf-8'))
    else:
        send.main(msg)
        kv.replace('msg',msg)
        return 'a new massage'+str(msg.encode('utf-8'))
