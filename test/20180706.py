# # class Student(object):
# #     s = Student()
# #     s.name = 'nana'
# #     print(s.name)
#
# # 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# # class Screen(object):
# #         #设置getwidth
# #     @property
# #     def width(self):
# #         return self._width
# #         # 设置setwidth
# #     @width.setter
# #     def width(self, v):
# #      if not isinstance(v, int):
# #         raise ValueError('width must be Integer!')
# #      if v <= 0:
# #         raise ValueError('width can not be 0!')
# #         self._width = v
# #         # 设置getheight
# #     @property
# #     def height(self):
# #         return self._height
# #     @height.setter
# #     def height(self, v):
# #      if not isinstance(v, int):
# #         raise ValueError('height must be Integer!')
# #      if v <= 0:
# #         raise ValueError('height can not be 0!')
# #      self._height = v
# #
# #     @property
# #     def resolution(self):
# #      return self._width * self._height
# #
# # s = Screen()
# # s.width = 1366
# # s.height = 768
# # print(s.resolution)
# # class Screen():
# #
# #     @property
# #     def width(self):
# #         return self._width
# #
# #     @width.setter
# #     def width(self,width):
# #         self._width = width
# #
# #     @property
# #     def height(self):
# #         return self._height
# #
# #     @height.setter
# #     def height(self,height):
# #         self._height = height
# #
# #     @property
# #     def resolution(self):
# #         return str(self._width) + ' * ' + str(self._height)
# #
# # s = Screen()
# # s.width = 1366
# # s.height = 768
# # print(s.resolution)
# class Animal(object):
#     pass
#
# # 大类:
# class Mammal(Animal):
#     pass
#
# class Bird(Animal):
#     pass
#
# # 各种动物:
# class Dog(Mammal):
#     pass
#
# class Bat(Mammal):
#     pass
#
# class Parrot(Bird):
#     pass
#
# class Ostrich(Bird):
#     pass
#
# class Runnable(object):
#     def run(self):
#         print('Running...')
#
# class Flyable(object):
#     def fly(self):
#         print('Flying...')
# class Dog(Mammal, Runnable):
#     pass
# class Bat(Mammal, Flyable):
#     pass
# class Student(object):
#     def __init__(self,name):
#         self.name= name
#     def __str__(self):
#         return 'Student object(name:%s)' % self.name
# print(Student('lyly'))


#
# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>100000:
#             raise StopIteration()
#         return self.a
#
# for i in Fib():
#     print(i)

#     #该看使用元类
#
# from functools import reduce
#
# def str2num(s):
#     try:
#         return int(s)
#     except ValueError as e:
#         print('ValueError')
#         return float(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
