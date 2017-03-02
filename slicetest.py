# -- coding: utf-8 --
#切片操作
L = ['a', 'b', 'c']
M = L[0:3]
N = L[:3]
O = L[-2:]
P = L[-2:-1]
R = range(10)
S = list(R)
S1 = S[:10:2]
S2 = S[::5]
print(M,N,O,P,R,S,S1,S2)
print('abcdefg'[::2])

