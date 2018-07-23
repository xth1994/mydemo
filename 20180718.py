# # import itertools
# # natual = itertools.count(1)
# # for n in natual:
# #     print(n)
#
#
# class Query(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Begin')
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
# from contextlib import contextmanager
#
# class Query(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
# @contextmanager
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')



#
# from urllib import request
# with request.urlopen('https://api.douban.com/v2/book/2129650')as f:
#     data = f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s'%(k,v))
#     print('Data',data.decode('utf-8'))



# from urllib import request
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent','Mozilla/6.0(iphone:CPU iphone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s'%(k,v))
#     print('Data:',f.read().decode('utf-8'))




# from urllib import  request,parse
# print('Login to weibo.cn....')
# email = input('Email:')
# passwd = input('Password:')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin','https://psssport.weibo.cn')
# req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
# with request.urlopen(req,data=login_data.encode('utf-8')) as f:
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s'%(k,v))
#     print('Data:',f.read().decode('utf-8'))
#
# from urllib import request
# import json
# def fetch_data(url):
#     with request.urlopen(url) as f:
#         js = json.load(f)
#         return json.loads(js.decode('utf-8'))
# URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
# data = fetch_data(URL)
# print(data)
# assert data['query']['results']['channel']['location']['city'] == 'Beijing'
# # print('ok')
# from html.parser import HTMLParser
# import re
# from urllib import request
# import urllib
#
# class PhythonEventParser(HTMLParser):
#     nameTagMark = False
#     locationTagMark = False
#     timeTagMark = False
#     eventInfo = {}
#     def handle_starttag(self,tag,attr):
#         if tag == 'h3':
#             self.nameTagMark = True
#         elif tag == 'time':
#             self.timeTagMark = True
#         elif tag == 'span':
#             self.locationTagMark = True
#     def handle_endtag(self,tag):
#         if tag == 'h3':
#             self.nameTagMark = False
#         elif tag == 'time':
#             self.timeTagMark = False
#         elif tag == 'span':
#             self.locationTagMark = False
#     def handle_data(self,data):
#         if self.nameTagMark:
#             self.eventInfo['event-title'] = data
#         if self.timeTagMark:
#             self.eventInfo['event-time'] = data
#         if self.locationTagMark:
#             self.eventInfo['event-location'] = data
#     def getEventInfo(self):
#         info = {}
#         for key,value in self.eventInfo.items():
#             info[key] = value
#         return info
#
# url = 'https://www.python.org/events/python-events/'
#
# with urllib.request.urlopen(url) as f:
#     data = f.read().decode('utf-8')
#     parser = PhythonEventParser()
#     re_li = r'<li>(.*?)</li>'
#     lis = re.findall(re_li,data,re.S|re.M)
#     pythonEvents = []
#     for li in lis:
#         parser.feed(data)
#         pythonEvents.append(parser.getEventInfo())
#         print('li: %s' % li)
#     print(pythonEvents)
#
# import requests
# from html.parser import HTMLParser
# from html.entities import name2codepoint
# import re
# try:
#     req=requests.get('https://www.python.org/events/python-events/')
# except:
#     print('没连上')
#
# res=req.text
# class myhtml(HTMLParser):
#     huizong=[]
#     datetime=[]
#     year=[]
#     adrss=[]
#     title=[]
#     """docstring for myhtml"""
#     def init(self):
#         HTMLParser.init(self)
#         self.flag=''
#
# def handle_starttag(self,tag,attrs):
#     if tag=='time' and attrs[0][0]=='datetime' and re.match('\d{4}-\d{2}-\d{2}T00:00:00\+00:00',attrs[0][1]):
#         self.flag=1
#     elif tag=='span':
#         for i in attrs:
#             if i[1]=='say-no-more':
#                 self.flag=2
#             elif i[1]=='event-location':
#                 self.flag=3
#     elif tag=='a':
#         for i in attrs:
#             if re.match(r'/events/python-events/\d{3}/',i[1]):
#                 self.flag=4
#
#     else:
#         self.flag=''
# def handle_data(self,data):
#     if self.flag==1:
#         myhtml.datetime.append(data)
#     elif self.flag==2 and re.match('\s\d{4}',data):
#         myhtml.year.append(data)
#     elif self.flag==3 and re.match('\w+',data):
#         myhtml.adrss.append(data)
#     elif self.flag==4 and re.match('\w+',data):
#         myhtml.title.append(data)
# def hz(self):
#     for i in range(8):
#         dict={}
#         dict['发布时间']=myhtml.datetime[i]
#         dict['发布年份']=myhtml.year[i]
#         dict['发布地址']=myhtml.adrss[i]
#         dict['发布标题']=myhtml.title[i]
#         myhtml.huizong.append(dict)
#     for i in myhtml.huizong:
#         print('发布年份：%s\n发布时间：%s\n发布标题：%s\n发布地址：%s\n********************\n'%(i['发布年份'],i['发布时间'],i['发布标题'],i['发布地址']))

#
# from PIL import Image
# im = Image.open('C:\\Users\\19645\\Desktop\\新建文件夹\\1.jpg')
# w,h=im.size
# print('Original image size:%sx%s'%(w,h))
# im.thumbnail((w//2,h//2))
# print('Resize image to:%sx%s'%(w//2,h//2))
# im.save('thumbnail.jpg','jpeg')

# from PIL import Image, ImageFilter
#
# # 打开一个jpg图像文件，注意是当前路径:
# im = Image.open('C:\\Users\\19645\\Desktop\\新建文件夹\\1.jpg')
# # 应用模糊滤镜:
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg', 'jpeg')


# from PIL import  Image,ImageDraw,ImageFont,ImageFilter
# import random
# def rndChar():
#     return  chr(random.randint(65,90))
# def rndColor():
#     return (random.randint(64,255),random.randint(64,255))
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# width =60*4
# height = 60
# image = Image.new('RGB',(width,height),(255,255,255))
# font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
# draw =ImageDraw.Draw(image)
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
#     # 输出文字:
#     for t in range(4):
#         draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
#     # 模糊:
#     image = image.filter(ImageFilter.BLUR)
#     image.save('code.jpg', 'jpeg')


# from tkinter import *
# class Application(Frame):
#     def __int__(self,master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()
#     def createWidegets(self):
#         self.helloLabel = Label(self, text='Hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()
# app =Application()
# app.master.geometry()
# app.master.title('Hello world')
# app.mainloop()
# from tkinter import *
# import tkinter.messagebox as messagebox
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)
#
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()


# 导入socket库:
import socket
import threading
import time

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# s.close()
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

# 监听端口:
# s.bind(('127.0.0.1', 9999))
# s.listen(5)
# print('Waiting for connection...')
#
# def tcplink(sock, addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)
# while True:
#     # 接受一个新连接:
#     sock, addr = s.accept()
#     # 创建新线程来处理TCP连接:
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()


#该看电子邮件模块