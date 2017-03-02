# -- coding: utf-8 --
#斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
    
#print(fib(3))
fib(5)
for n in fib(5):
    print(n)
    
#杨辉三角
def triangles(max):
    L = [1]
    n = 0
    while n < max:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
        n = n + 1
        
for L in triangles(10):
    print(L)
        

