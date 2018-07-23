# # #以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
# # def product(*number):
# #     if number:
# #         n=1
# #         for i in number:
# #             n=n*i
# #             return n
# #         else:
# #             int(number)
# #
# # print(product(34))
# # def product(x, *args):
# #     for i in args:
# #         if not isinstance(i, (int, float)):
# #             raise TypeError("bad operand type")
# #         x *= i
# #     return x
#
# #
# # def move(n,a,b,c):
# #     if n ==1:
# #         print(a,'---->',b);
# #     else:
# #         move(n-1,a,c,b)
# #         move(1,a,b,c)
# #         move(n-1,b,a,c)
# # print(move(4,'A','B','C'))
#
# #
# # L =[]
# # n=1
# # while n<=99:
# #     L.append(n)
# #     n=n+2
# # print(L)
#
# # L=list(range(100))
# # print(L[:10])
# # -*- coding: utf-8 -*-
# # def trim(s):
# #     if (s[:1]==''):
# #         return trim(s[1:])
# #     elif s[-1:]=='':
# #         return trim(s[:-2])
# #     else:
# #         return s
# # print(trim(" hello "))
#
# # def findMinAndMax(L):
# #     max=L[0]
# #     min=L[0]
# #     for i in L:
# #         if i > max:
# #             max = i
# #         elif i < min:
# #             min = i
# #     print('min:%s,max:%s' % (min,max))
# # L = [25, 6, 34, 5, 21, 66, 29, 12]
# # findMinAndMax(L)
#
# # L1 = ['Hello', 'World', 18, 'Apple', None]
# # L2 = [x.lower() for x in L1 if isinstance(x,str)]
# # print(L2)
#
# # L = [x * x for x in range(10)]
# # print(L)
# # G = (x * x for x in range(10))
# #
# # for n in G:
# #     print(n)
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L= [(L + [0])[i] + ([0] + L)[i] for i in range(len(L)+1)]
# #
# # def triangles():
# #     x=[0,1,0]
# #     s=[1]
# #     yield(s)
# #     while True:
# #         s=[]#设定一个空的数列，此数列每次跳到下一行时候刷新为空数列，用来存放新数列
# #         for j in range(0,len(x)-1):#在每一次循环中控制杨辉三角每一行的数字
# #             s.append(x[j]+x[j+1])
# #         x=[0]+s+[0]#让x首尾增加[0]元素，以便下一行调用的时候使用。
# #         yield(s)
# # for n in triangles():
# #     print(n)
# # def add(x, y, f):
# #     return f(x) + f(y)
# #
# # print(add(-5, 6, abs))
# def normalize(name):
#     return name[0].upper() + name[1:].lower()
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
#
#
# def prod(L):
#     return reduce(lambda x,y : x * y ,L)
#
#
#
# def power(x, n):
#     c = 1
#     while n > 0:
#         n = n - 1
#         c = c * x
#     return c
# digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def a (s) :
#     return digits[s]
# n = len (s.split('.')[1])
# m = s.split('.')[0] + s.split('.')[1]
# M = reduce(lambda x, y: x * 10 + y, map(a, m))
# return M / power(10,n)
# def is_odd(n):
#     return  n%2==1
# s=list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))

# def not_empty(s):
#     return  s and s.strip()
# s=list(filter(not_empty,['A','B',None,'C','  ']))
#
# print(s)
# def is_palindrome(n):
#     s = str(n)
#     return s == s[::-1]
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print




# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0].lower()
#
# def by_score(t):
#     return -t[1]
# L2 = sorted(L, key=by_name)
# print(L2)
# L3 = sorted(L, key=by_score)
# print(L3)

#
# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#         return ax
# print(12)
# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return  i*i
#         fs.append(f)
#     return fs
# f1,f2,f3=count()
# # print(f1())
#
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g()
#     fs =[]
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs
# f1,f2,f3=count()
# print(f1())
def is_odd(n):
    return n % 2 == 1


L = list(filter(lambda  n:n%2 == 1, range(1,20)))
print(L)