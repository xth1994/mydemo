# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(is_odd, range(1, 20)))
# print(L)
#
#
# L2 =list(filter(lambda  x:x % 2==1 ,range(1,20)))
# print(L2)

#
#
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('call %s():' % func.__name__)
#             return func(*args, **kw)
#         return  wrapper
#     return decorator
# @log('execute')
# def now():
#     print('2015-3-25')
# print(now.__name__)

# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print('call %s():' %func.__name__)
#         return  func(*args,**kw)
#     return wrapper
# import functools
#
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# -*- coding: utf-8 -*-
# import time, functools
# def metric(fn):
#     def decorator(func):
#            @functools.wraps(func)
#            def wrapper(*args, **kw):
#                 print('%s executed in %s ms' % (fn.__name__, 10.24))
#                 return func(*args, **kw)
#            return wrapper
#     return decorator
# # 测试
# @metric
# def fast(x):
#     time.sleep(0.0012)
#     return x;
#
# @metric
# def slow(x):
#     time.sleep(0.1234)
#     return x;
#
# f = fast(11)
# s = slow(11)
# if f != 11:
#     print('测试失败!')
# elif s != 11:
#     print('测试失败!')
# -*- coding: utf-8 -*-
# import time, functools
#
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         startTime = time.time()
#         fn(*args, **kw)
#         diffTime = (time.time() - startTime)*1000
#         print('%s 运行了 %s ms' % (fn.__name__, diffTime))
#         return fn(*args, **kw)
#     return wrapper
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')


# import functools
# int2 = functools.partial(int,base=2)
# # in2('10000')
# class Student(object):
#     def  __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def print_score(self):
#         print('%s:%s' % (self.name,self.score))
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#     def get__gender(self):
#         return self.__gender
#     def set_gender(self,gender):
#         if gender=='男' or gender =='女':
#             self.__gender = gender
#         else:
#             return  ValueError('Error Gender')
# bart = Student('Bart Simpson','男')
# print(bart.name)
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
# class dog(Animal):
#     pass
# class cat(Animal):
#     pass
# Dog = dog()
# Dog.run()
# Cat =cat()
# Cat.run()

# 龙鸣写法：
#
# count = 0
# class Student(object):
#     def __init__(self,name):
#         self.name = name
#         global count
#         count+=1
#
# # 贵族写法：
#
# class Student(object):
#     count = 0
#     def __init__(self,name):
#         self.name=name
#         Student.count+=1
# 下面该看面向对象高级编程