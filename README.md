# lkong2weibo
一个简单的抓取http://www.yousuu.com/comments/上书评并发布到微博上的python脚本。抓取部分使用的是beautifulsoup。
目前已知的问题就是如果cron上的频率设置太高，就会被微博封锁，暂时打算采用高大上的异步方法（或许叫这个名字吧），就是抓取三次。
发送一次（因为优书网本身并未有相应的限制）
