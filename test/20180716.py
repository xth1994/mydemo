# try:
#    f = open('C:/Users/19645\Desktop/新建文件夹/1.txt','r')
#    s =f.read()
#    print(s)
# finally:
#     if f:
#        f.close()
# with open('C:/Users/19645\Desktop/新建文件夹/1.txt','r') as f:
#     print(f.read())

# f = open('C:/Users/19645\Desktop/新建文件夹/1.txt','w')
# f.write('hello,world!')
# f.close()
# with open('C:/Users/19645\Desktop/新建文件夹/1.txt','a') as f:
#     f.write('sadsas')

# fpath = r'C:/Users/19645\Desktop/新建文件夹/1.txt'
#
# with open(fpath, 'r') as f:
#     s = f.read()
#     print(s)

# from io import StringIO
# f = StringIO()
# print(f.write('hello'))
# print(f.getvalue())
#
# from io import StringIO
# f = StringIO('hello\n hi!\n')
# while True:
#     s = f.readline()
#     if s =='':
#         break
#     print(s.strip())


# from  io import  BytesIO
# f = BytesIO()
# f.write(('中文'.encode('utf-8')))
# print(f.getvalue())


# from  io import  BytesIO
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())
#
# import os
# print(os.name)
#
# import os
# def dir_l(path = '.'):
#     if path == '.':
#         L = os.listdir(os.path.abspath(path))
#     else:
#         L = os.listdir(path)
#     for dir in L:
#         dir = os.path.join(path,dir)
#         if os.path.isdir(dir):
#             print(dir)
# path = input('请输入一个文件夹路径，如果不输入则默认当前目录：')
#
# dir_l(path)

#
# import json
# d = dict(name='Bob',age=20,score=88)
# print(json.dumps(d))
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# json.loads(json_str)


# import json
# class Student(object):
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score
#     def student2dict(std):
#         return {
#             'name':std.name,
#             'age':std.age,
#             'score':std.score
#         }
# s = Student('Bob',20,88)
# print(json.dumps(s, default=Student.student2dict))
# print(json.dumps(s, default=lambda obj: obj.__dict__))


# import  os
# print('Process(%s) start....'% os.getpid())
# pid = os.fork()
# if pid ==0:
#     print('I am child process (%s) and my parent is %s.' %(os.getpgid(),os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# from multiprocessing import Process
# import os
# def run_proc(name):
#     print('Run child process %s(%s)...' %(name,os.getppid()))
# if __name__ =='__main__':
#     print('Parent process %s.' % os.getpid())
#     p =  Process(target=run_proc,args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end')

from multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print('Run task %s(%s)...'%(name,os.getppid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' %(name,(end -start)))
if __name__ =='__main__':
    print('Parent process %s' % os.getppid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All sunprocesses done.')




    #该看子进程