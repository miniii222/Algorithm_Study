# -*- coding: utf-8 -*-
"""
https://www.acmicpc.net/problem/2749
"""
n = int(input())

#%% recursive -> 오래 걸림
def fibonacci(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
#%% 시간초과 ㅎㅎ
n = 1000
a = 0; b = 1

for i in range(n-1) :
    a,b = b, a+b

print(b%1000000)