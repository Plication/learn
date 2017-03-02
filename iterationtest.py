# -- coding: utf-8 --
from collections import Iterable
#迭代操作
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#迭代key
for key in d:
    print(key)
#迭代value。为什么迭代出的值都是同一个？
for value in d.values():
    print(value)
#同时迭代key和value    
for k, v in d.items():
    print(key,value)
#迭代字符串
for ch in 'abcdefg':
    print(ch)
    
#判断是否可迭代,返回Ture/False
print(isinstance('abcd',Iterable))

#enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['a', 'b', 1, 'd']):
    print(i, value)
#for循环里，同时引用了两个变量，在Python里是很常见的    
for x, y in [(1, 2), (3, 4)]:
    print(x, y)
    
