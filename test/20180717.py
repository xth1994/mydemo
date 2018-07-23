# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call('nslookup','www.python.org')
# print('exit code',r)
#
# nslookup www.python.org


# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

#
# from multiprocessing import Process,Queue
# import  os,time,random
# #写数据进程代码
# def write(q):
#     print('Process to write:%s' % os.getpid())
#     for value in['A','B','C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
# #读数据进程代码
# def read(q):
#     print('Process to read:%s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
# if __name__=='__main__':
#     #父进程创建 Queue,并传给各个子进程
#     q =   Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#     #启动子进程pw.写入
#     pw.start()
#     # 启动子进程pr,读取
#     pr.start()
#     #等待pw结束
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()
#
# import time,threading
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n<5:
#         n=n+1
#         print('thread %s >>>%s' %(threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
# print('thread %s is running....' % threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


#
# import  threading
# local_school = threading.local()
# def process_student():
#     std = local_school.student
#     print('Hello,%s(in%s)' %(std,threading.current_thread().name))
# def process_thread(name):
#     local_school.student = name
#     process_student()
# t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
# t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# task_master.py

# import random, time, queue
# from multiprocessing.managers import BaseManager
#
# # 发送任务的队列:
# task_queue = queue.Queue()
# # 接收结果的队列:
# result_queue = queue.Queue()
#
# # 从BaseManager继承的QueueManager:
# class QueueManager(BaseManager):
#     pass
#
# # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)
# # 绑定端口5000, 设置验证码'abc':
# manager = QueueManager(address=('', 5000), authkey=b'abc')
# # 启动Queue:
# manager.start()
# # 获得通过网络访问的Queue对象:
# task = manager.get_task_queue()
# result = manager.get_result_queue()
# # 放几个任务进去:
# for i in range(10):
#     n = random.randint(0, 10000)
#     print('Put task %d...' % n)
#     task.put(n)
# # 从result队列读取结果:
# print('Try get results...')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result: %s' % r)
# # 关闭:
# manager.shutdown()
# print('master exit.')

# -*- coding: utf-8 -*-
# import re
# def is_valid_email(addr):
#     if re.match(r'^[0-9a-zA-Z_.]+@[a-z]+.com$', addr):
#         return "匹配成功"
#     else:
#         return "匹配失败"
#
#
# # 测试:
# print(is_valid_email("someone@gmail.com"))
# print(is_valid_email('bill.gates@microsoft.com'))
# print(is_valid_email('bob#example.com'))
# print(is_valid_email('mr-bob@example.com'))
#
# re_email = re.compile(r'^[0-9a-zA-Z\.]+@[a-z]+(.com)$')
# return re_email.match(addr)

#
# # -*- coding: utf-8 -*-
# import re
# def name_of_email(addr):
#     re_name = re.compile(r'(<?)([a-zA-Z\s]*)(>?)(\s?)(\w*)@(\w+)(.org)$')
#     return re_name.match(addr).group(2)
# assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
# assert name_of_email('tom@voyager.org') == 'tom'
# print('ok')


# from datetime import datetime
# now = datetime.now()
# print(now)


# from datetime import datetime
# dt = datetime(2015,4,9,19,12,20)
# t = 1428372900.0
# print(dt.timestamp())
# print(datetime.fromtimestamp(t))



# from datetime import datetime
# cday = datetime.strptime('2015-6-3 18:22:34','%Y-%m-%d %H:%M:%S')
# print(cday)
#
# from datetime import datetime
# now = datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))


# -*- coding:utf-8 -*-

# import re
# from datetime import datetime, timezone, timedelta
# def to_timestamp(dt_str, tz_str):
#     time = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
#     re_zone = re.compile(r'UTC([+|-]\d+):(\d+)')
#     zone = int(re_zone.match(tz_str).group(1))
#     return time.replace(tzinfo=timezone(timedelta(hours=zone))).timestamp()
#
#
# # 测试:
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0, t1
#
# t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# assert t2 == 1433121030.0, t2
#
# print('ok')


# -*- coding: utf-8 -*-
# import base64
# def safe_base64_decode(s):
#     if len(s) % 4 != 0:
#         s += b"=" * (len(s) - len(s) // 4 * 4)
#     return base64.b64decode(s)
# # 测试:
# assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
# # assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
# # print('ok')
#
# # -*- coding: utf-8 -*-
# import base64, struct
# bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
# def bmp_info(data):
#     return {
#         'width': 200,
#         'height': 100,
#         'color': 24
#     }
# def bmp_info(data):
#     tu = struct.unpack('<ccIIIIIIHH', data[:30])
#     if tu[0] == b'B' and tu[1] == b'M':
#         return {
#             'width': tu[6],
#             'height': tu[7],
#             'color': tu[9]
#         }
#     return None

# # 测试
# bi = bmp_info(bmp_data)
# assert bi['width'] == 28
# assert bi['height'] == 10
# assert bi['color'] == 16
# print('ok')
#
#
# import hashlib
# md5 = hashlib.md5()
# md5.update('how to use md5 in python 1ashlib?'.encode('utf-8'))
# print(md5.hexdigest())
#
# import hashlib
#
# md5 = hashlib.md5()
# md5.update('how to use md5 in '.encode('utf-8'))
# md5.update('python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
#
#
# #128字节
# import hashlib
#
# md5 = hashlib.md5()
# md5.update('how to use md5 in '.encode('utf-8'))
# md5.update('python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
# #160 bit字节



# # -*- coding: utf-8 -*-
# import hashlib
# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
# def login(user,password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     print('md5password: %s' % md5.hexdigest())
#     return db[user] == md5.hexdigest()
# def login(user, password):
#     pass
# # 测试:
# login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')

# -*- coding: utf-8 -*-
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
def login(username, password):
    user = db[username]
    return user.password == get_md5(password)
def login(username,password):
    user = db[username]
    return user.password == get_md5(password + user.salt)

# 测试:
login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
print('ok')



#该看常用内建模块的intertoolsl
