# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# a =100
# if a>0:
#     print(a)
# else:
#     print(-a)




# # -*- coding: utf-8 -*-
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# print(n,f,s1,s2,s3,s4)


# s1=72
# s2=85
# r=(s2-s1)/s1*100
# print('提高了%d    %%'%(r))




# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # # 打印Lisa:
# print(L[2][2])

# h=float(input("请输入身高"))
# w=float(input("请输入体重"))
# s=w/(h*h)
# print(s)
# if s<18.5:
#     print('过轻')
# elif 18.5>=s and s<25:
#     print('正常')
# elif 25>=s and s<28:
#     print('过重')
# elif 28>=s and s<32:
#     print('肥胖')
# else:
#     print('过重')


# sum=0
# for i in  range(101):
#     sum = sum +i
# print(sum)


# L = ['Bart', 'Lisa', 'Adam']
# for i in L:
#     print("你好"+i)

# A =0
# for i in range(100):
#     if i%2==1:
#         print(i)
#     else:
#         pass
#
#

# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(hex(n2))


import math

def quadratic(a,b,c):
    if not (isinstance(a,(int,float))and isinstance(b,(int,float))and isinstance(c,(int,float))):
        raise TypeError('你输入的是错误的计算对象类型')
    delta = pow(b, 2) - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2
    elif delta == 0:
        return -b / (2 * a)
    else:
        return None