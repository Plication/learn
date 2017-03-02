# -- coding: utf-8 --
#生成0到10的列表
L = list(range(1, 11))
print(L)

#用列表生成式（List Comprehensions)生成[1x1, 2x2, 3x3, ..., 10x10]
L1 = [x * x for x in range(1, 11)]
print(L1)

#上面列表只含偶数平方的列表
L2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L2)

L3 = [m + n for m in 'abc' for n in 'xyz']
print(L3)


import os
print([d for d in os.listdir('.')])# os.listdir可以列出文件和目录

#使用dict的两个变量key和value来生成一个list
d = {'a': 'A', 'b': 'B', 'c': 'C'}
print([k + '=' + v for k, v in d.items()])

#lower()方法将所有的字符串变成小写
l = ['HELLO', 'WORLD']
print([s.lower() for s in l])

x = 'abc'
print(isinstance(x, str))

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str) == True]
print(L2)
L3=[str(x).lower() for x in L1]
print(L3)
